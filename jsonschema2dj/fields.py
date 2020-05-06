"""helper methods for field level schema to django field like object
"""
from typing import List, Dict, Any, Tuple
import keyword
import warnings


def stringify(key, value):
    if key in ("RegexValidator",) and value is not None:
        return f'"{value}"'
    if key == "validators":
        return "[" + ", ".join(f"validators.{a}({stringify(a, b)})" for a, b in value.items()) + "]"
    return value


class Field:
    """A dict that doesnt store certain django specific keys
    and values that have default values.

    This is not strictly necessary but produces slightly nicer
    looking code.
    """

    @property
    def jinja(self):
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
        if self.type in ("IntegerField", "DecimalField", "DateField", "DateTimeField",):
            return ["exact", "gte", "lte"]
        elif self.is_enum:
            return ["exact", "in"]
        return []


class Relationship(Field):
    def __init__(self, type, name, to, null=False):
        self.to = to
        self.null = null
        super().__init__(type, name, null=null)

    @property
    def jinja(self):
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
        super().__init__("JSONField", *args, **kwargs)

    @property
    def jinja(self):
        name = f"_{self.name}" if keyword.iskeyword(self.name) else self.name
        verbose_name = f'"{self.name}", ' if keyword.iskeyword(self.name) else ""
        return f'{name} = JSONField({verbose_name}validators=[JSONSchemaValidator({self.options["schema"]}, DEFINITIONS)])'


def build_value_validators(sch: Dict) -> Dict:
    """common to integers and strings"""
    validators = {}
    if "minimum" in sch:
        validators["MinValueValidator"] = sch["minimum"]
    if "maximum" in sch:
        validators["MaxValueValidator"] = sch["maximum"]
    return validators


def build_choices(name: str, enums) -> Field:
    "helper function for enums to choices"
    if all(isinstance(enum, str) for enum in enums):
        names = [value.lower().replace(" ", "_") for value in enums]
        return Field(
            "CharField",
            name,
            max_length=max(map(len, enums)),
            choices=list(zip(names, enums)),
        )

    if all(isinstance(enum, int) for enum in enums):
        return Field("IntegerField", name, choices=list(zip(map(str, enums), enums)))

    raise NotImplementedError("only integer or string enums are supported")


def build_string_field(
    name: str, sch: Dict, null: bool, primary_key: bool, default: str, description: str
) -> Field:
    "the string case is complex enough to have its own function"
    options = dict(
        null=null, primary_key=primary_key, default=default, help_text=description,
    )
    validators = {}

    max_length = sch.get("maxLength", 255)
    min_length = sch.get("minLength")

    options.update(max_length=max_length)

    if min_length:
        validators["MinLengthValidator"] = min_length

    if (min_length and max_length <= min_length) or max_length > 255:
        return Field("TextField", name, type="TextField", **options)

    if sch.get("enum"):
        options.update(build_choices(name, sch.get("enum")).options)

    if sch.get("pattern"):
        validators["RegexValidator"] = f"{sch.get('pattern')}"

    if validators:
        options.update(validators=validators)

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
            return Field(
                formats.get(sch["format"], "CharField"),
                name,
                null=options.get("null", False),
                primary_key=primary_key,
                default=default,
                help_text=description,
                max_length=255,
            )

        return Field(
            formats.get(sch["format"], "CharField"),
            name,
            null=options.get("null", False),
            primary_key=primary_key,
            default=default,
            help_text=description,
        )

    return Field("CharField", name, **options)


def rationalize_type(sch: Dict) -> Tuple[str, Dict, bool, Any, str]:
    """the type is problematic especially with regards to enums and null"""
    null = False
    default = sch.get("default")
    description = sch.get("description")
    if description:
        description = f'"""{description}"""'

    if sch.get("type"):
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
        return _type, sch, null, default, description

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
        return _type, sch, null, default, description

    if "$ref" in sch or "const" in sch or "properties" in sch:
        return "object", sch, null, default, description

    if "items" in sch:
        return "items", sch, null, default, description

    raise ValueError(
        "either the type must be specified or it must be an enum or a $ref, const, items, or properties",
        sch,
    )


def build_field(name: str, schema: Dict, required: List) -> Field:
    """this is the entry point for the module"""

    primary_key = (name == required[0]) if required else False

    field_type, schema, null, default, description = rationalize_type(schema)

    null = null or name not in required

    if name == "id":
        if schema.get("type") != "string" and schema.get("format") != "uuid":
            return JSONField(
                name, schema=schema
            )  # "field with name id must be a UUID", sch)
        return Field(
            "UUIDField",
            name,
            default=default or "uuid.uuid4",
            primary_key=True,
            help_text=description,
        )

    if field_type == "string":
        return build_string_field(name, schema, null, primary_key, default, description)

    if field_type == "integer":
        validators = build_value_validators(schema)
        return Field(
            "IntegerField",
            name,
            null=null,
            validators=validators,
            primary_key=primary_key,
            default=default,
            help_text=description,
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

    return JSONField(name, schema=schema, default=default, help_text=description,)
