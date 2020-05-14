"""helper methods for field level schema to django field like object
"""
from typing import List, Dict, Any, Tuple
import keyword
import warnings


def stringify(key, value):
    if key == "RegexValidator" and value is not None:
        return f"'{value}'"
    if key == "validators":
        return "[" + ", ".join(f"validators.{a}({stringify(a, b)})" for a, b in value.items()) + "]"
    return value


class Field:
    """A glorified dict that doesnt store certain django specific keys
    and values that have default values.

    This is not strictly necessary but produces slightly nicer
    looking code.
    """

    def __repr__(self):
        """this is critical for use in the jinja template
        """
        _name = f"_{self.name}" if keyword.iskeyword(self.name) else self.name
        verbose_name = f'"{self.name}", ' if keyword.iskeyword(self.name) else ""

        _options = ", ".join(
            f"{key}={stringify(key, value)}" for key, value in self.options.items()
        )
        return f"{_name} = models.{self.type}({verbose_name}{_options})"

    def __init__(self, django_type: str, name: str, **kwargs: Any) -> None:
        self.type = django_type
        self.name = name
        self.options = {}
        for key, value in kwargs.items():
            if key in ("default", "help_text") and value is None:
                pass
            elif key in ("null", "primary_key") and not value:
                pass
            elif key == "type":
                raise TypeError("type cannot be specified in the kwargs")
            else:
                self.options[key] = value

    @property
    def is_enum(self):
        return "choices" in self.options

    @property
    def is_text_search(self):
        return self.type == "CharField" and "choices" not in self.options

    @property
    def filter_type(self):
        if self.type in ("IntegerField", "DecimalField", "DateField", "DateTimeField"):
            return ["exact", "gte", "lte"]
        elif self.is_enum:
            return ["exact", "in"]
        return []


class Relationship(Field):
    def __init__(self, type, name, to, null=False):
        self.to = to
        self.null = null
        super().__init__(type, name, null=null)

    def __repr__(self):
        name = f"_{self.name}" if keyword.iskeyword(self.name) else self.name
        options = dict(self.options)
        if keyword.iskeyword(self.name):
            options.update(verbose_name=f'"{self.name}"')

        if self.type != "ManyToManyField":
            options.update(on_delete="models.CASCADE")

        options = ", ".join([f'"{self.to}"'] + [f"{k}={v}" for k, v in options.items()])

        return f"{name} = models.{self.type}({options})"


class JSONField(Field):
    def __init__(self, *args, **kwargs):
        self.schema = kwargs["schema"]
        if "items" in self.schema:
            self.to = self.schema["items"].get("$ref", "").split("/")[-1] or None
            self.default = "list"
        else:
            self.to = self.schema.get("$ref", "").split("/")[-1] or None
            self.default = "dict"
        super().__init__("JSONField", *args, **kwargs)

    def __repr__(self):
        name = f"_{self.name}" if keyword.iskeyword(self.name) else self.name
        verbose_name = f'"{self.name}", ' if keyword.iskeyword(self.name) else ""

        options = dict(default=self.default)
        if self.options.get("null", False):
            options["null"] = True

        options = ", ".join(f"{k} = {v}" for k, v in options.items())

        return f"{name} = JSONField({verbose_name}{options}, validators=[JSONSchemaValidator({self.schema}, DEFINITIONS)])"


def build_value_validators(sch: Dict) -> Dict:
    """common to integers and strings"""
    validators = {}
    if "minimum" in sch:
        validators["MinValueValidator"] = sch["minimum"]
    if "maximum" in sch:
        validators["MaxValueValidator"] = sch["maximum"]
    return validators


def build_string_field(
    name: str, sch: Dict, null: bool, primary_key: bool, default=None, description=None
) -> Field:
    "the string case is complex enough to have its own function"
    options = dict(
        null=null, primary_key=primary_key, default=default, help_text=description
    )
    validators = {}

    max_length = sch.get("maxLength", 255)
    min_length = sch.get("minLength")

    options.update(max_length=max_length)

    if min_length:
        validators["MinLengthValidator"] = min_length

    if (min_length and max_length <= min_length) or max_length > 255:
        # if max_length is unknown or too large then this cant be a CharField
        return Field("TextField", name, type="TextField", **options)

    if "enum" in sch:
        enums = sch["enum"]
        names = [value.lower().replace(" ", "_") for value in enums]
        options.update(max_length=max(map(len, enums)), choices=list(zip(names, enums)))

    if sch.get("pattern"):
        validators["RegexValidator"] = f"{sch.get('pattern')}"

    if validators:
        options.update(validators=validators)

    if name.upper() == "ID":
        options.update(primary_key=True, null=False, default=default or "uuid.uuid4")

    if sch.get("format"):

        formats = {
            "date-time": "DateTimeField",
            "date": "DateField",
            "time": "TimeField",
            "email": "EmailField",
            "idn-email": "EmailField",
            "ipv4": "GenericIPAddressField",
            "ipv6": "GenericIPAddressField",
            "uuid": "UUIDField",
        }
        if sch["format"] not in formats:
            warnings.warn(f"no code written to handle format: {sch.get('format')}")
            # if max_length is unknown or too large then this cant be a CharField
            return Field(formats.get(sch["format"], "TextField"), name, **options)

        options.pop("max_length")

        return Field(formats.get(sch["format"], "CharField"), name, **options)

    return Field("CharField", name, **options)


def rationalize_type(name: str, sch: Dict, required: List[str]) -> Tuple[str, bool]:
    """the type is problematic especially with regards to enums and null"""
    null = name not in required

    if "type" in sch:
        _type = sch.get("type")
        if isinstance(_type, list):
            if len(sch["type"]) == 0 or len(_type) > 2 or len(_type) == 2 and "null" not in _type:
                raise ValueError(
                    "if type is a list it should either contain 1 element, or 2 where one is null"
                )
            if len(_type) == 1:
                _type = _type[0]
            else:
                null = True
                _type = next(x for x in _type if x != "null")
        return _type, null

    if sch.get("enum"):
        enums = sch.get("enum", [])
        if "null" in enums:
            enums.remove("null")
            null = True

        if all(isinstance(enum, int) for enum in enums):
            _type = "integer"
        elif all(isinstance(enum, str) for enum in enums):
            _type = "string"
        else:
            raise ValueError(
                "all values in an enum must be either all strings or all integers"
            )
        return _type, null

    raise ValueError("not possible to determine simple-field type")


def build_field(name: str, schema: Dict, required: List) -> Field:
    """this is the entry point for the module"""

    primary_key = False

    field_type, null = rationalize_type(name, schema, required)

    default = schema.get("default")

    description = schema.get("description")
    if description:
        description = repr(description).replace("\n", "\\n")

    if name.upper() == "ID":
        primary_key = True
        null = False

    if field_type == "string":
        return build_string_field(name, schema, null, primary_key, default, description)

    if field_type == "integer":
        validators = build_value_validators(schema)

        options = {}
        if "enum" in schema:
            options["choices"] = [(e, e) for e in schema["enum"]]

        return Field(
            "IntegerField",
            name,
            null=null,
            validators=validators,
            primary_key=primary_key,
            default=default,
            help_text=description,
            **options,
        )

    if field_type == "number":
        validators = build_value_validators(schema)
        return Field(
            "DecimalField",
            name,
            null=null,
            validators=validators,
            max_digits=10,
            decimal_places=5,
            primary_key=primary_key,
            default=default,
            help_text=description,
        )

    if field_type == "boolean":
        return Field(
            "BooleanField",
            name,
            null=null,
            primary_key=primary_key,
            default=default,
            help_text=description,
        )

    raise ValueError(f"field-type: {field_type} is not supported")
