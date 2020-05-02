"""helper methods for field level schema to django field like object
"""
from typing import List, Dict, Any, Tuple, Optional

from jsonschema2dj.relationships import FieldDict


def build_value_validators(sch: Dict) -> Dict:
    """common to integers and strings"""
    validators = {}
    if "minimum" in sch:
        validators["MinValueValidator"] = sch["minimum"]
    if "maximum" in sch:
        validators["MaxValueValidator"] = sch["maximum"]
    return validators


def build_choices(enums, _type:str="string") -> FieldDict:
    "helper function for enums to choices"
    if _type == "string":
        names = [value.lower().replace(" ", "_") for value in enums]
        return FieldDict(
            max_length=max(map(len, enums)), choices=list(zip(names, enums))
        )

    if _type == "integer":
        return FieldDict(choices=list(zip(map(str, enums), enums)))

    raise NotImplementedError("only integer or string enums are supported")


def build_string_field(sch: Dict, null: bool, primary_key: bool, default: str, description: str) -> FieldDict:
    "the string case is complex enough to have its own function"
    field = FieldDict(
        null=null, primary_key=primary_key, default=default, label=description
    )
    validators = {}

    max_length = sch.get("maxLength", 255)
    min_length = sch.get("minLength")

    field.options.update(max_length=max_length)

    if min_length:
        validators["MinLengthValidator"] = min_length

    if (min_length and max_length <= min_length) or max_length > 255:
        return FieldDict(type="TextField", **field.options)

    if sch.get("enum"):
        field.options.update(build_choices(sch.get("enum")).options)

    if sch.get("pattern"):
        validators["RegexValidator"] = f"{sch.get('pattern')}"

    if validators:
        field.options.update(validators=validators)

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
        try:
            return FieldDict(
                type=formats[sch["format"]],
                null=field.options.get("null", False),
                primary_key=primary_key,
                default=default,
                label=sch.get("description"),
            )
        except KeyError:
            raise NotImplementedError(
                f"no code written to handle format: {sch.get('format')}"
            )

    return FieldDict(type="CharField", **field.options)


def rationalize_type(sch: Dict) -> Tuple[str, Dict, bool, Any, str]:
    """the type is problematic especially with regards to enums and null"""
    null = False
    default = sch.get("default")
    description = sch.get("description")
    if description:
        description =description.replace('\n', '\\n')

    if sch.get("type"):
        _type = sch.get("type")
        if isinstance(_type, list):
            if (
                len(sch["type"]) == 0
                or len(_type) > 2
                or len(_type) == 2
                and "null" not in _type
            ):
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

    if "$ref" in sch or "const" in sch:
        return "object", sch, null, default, description

    raise ValueError("either the type must be specified or it must be an enum or a $ref or a const", sch)


def build_field(name: str, sch: Dict, required: List) -> FieldDict:
    """this is the entry point for the module"""

    primary_key = (name == required[0]) if required else False

    field_type, sch, null, default, description = rationalize_type(sch)

    if name == "id":
        if sch.get("type") != "string" and sch.get("format") != "uuid":
            return FieldDict(type="JSONField", schema=sch) #"field with name id must be a UUID", sch)
        return FieldDict(
            type="UUIDField",
            default=default or "uuid.uuid4",
            primary_key=primary_key,
            label=description,
        )

    if field_type == "string":
        return build_string_field(sch, null, primary_key, default, description)

    if field_type == "integer":
        validators = build_value_validators(sch)
        return FieldDict(
            type="IntegerField",
            null=null,
            validators=validators,
            primary_key=primary_key,
            default=default,
            label=description,
        )

    if field_type == "number":
        validators = build_value_validators(sch)
        return FieldDict(
            type="DecimalField",
            null=null,
            validators=validators,
            max_digits=10,
            decimal_places=5,
            primary_key=primary_key,
            default=default,
            label=description,
        )

    if field_type == "boolean":
        return FieldDict(
            type="BooleanField",
            null=null,
            primary_key=primary_key,
            default=default,
            label=description,
        )

    return FieldDict(type="JSONField", schema=sch, default=default, label=description)
