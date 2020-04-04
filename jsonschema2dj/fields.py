"""helper methods for field level schema to django field like object
"""


def build_value_validators(sch):
    """common to integers and strings"""
    validators = []
    if "minimum" in sch:
        validators.append(("MinValueValidator", sch["minimum"]))
    if "maximum" in sch:
        validators.append(("MaxValueValidator", sch["maximum"]))
    return validators


def build_choices(sch, _type="string"):
    "helper function for enums to choices"
    if _type == "string":
        names = [value.lower().replace(" ", "_") for value in sch["enum"]]
        return dict(
            max_length=max(map(len, sch["enum"])), choices=list(zip(names, sch["enum"]))
        )

    if _type == "integer":
        names = list(map(str, sch["enum"]))
        return dict(choices=list(zip(names, sch["enum"])))

    raise NotImplementedError("only integer or string enums are supported")


def build_string_field(sch, null):
    "the string case is complex enough to have its own function"
    options = dict(null=null)
    validators = []

    max_length = sch.get("maxLength", 255)
    min_length = sch.get("minLength")

    options.update(max_length=max_length)

    if min_length:
        validators.append(("MinLengthValidator", min_length))

    if (min_length and max_length <= min_length) or max_length > 255:
        return "TextField", options

    if "enum" in sch:
        options.update(build_choices(sch))

    pattern = sch.get("pattern")
    if pattern:
        validators.append(("RegexValidator", f'r"{pattern}"'))

    if validators:
        options.update(validators=validators)

    _format = sch.get("format")
    if _format is None:
        return "CharField", options

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
        return formats[_format], dict(null=options["null"])
    except KeyError:
        raise NotImplementedError(f"no code written to handle format: {_format}")


def rationalize_type(sch, null):
    """the type is problematic especially with regards to enums and null"""
    _type = sch.get("type")
    if _type:
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
        return _type, sch, null

    if "enum" in sch:
        if "null" in sch["enum"]:
            sch["enum"].remove("null")
            null = True

        if all(isinstance(enum, int) for enum in sch["enum"]):
            _type = "integer"
        elif all(isinstance(enum, str) for enum in sch["enum"]):
            _type = "string"
        else:
            raise ValueError(
                "all values in an enum must be either all strings or all integers"
            )
        return _type, sch, null

    raise ValueError(f"either the type must be specified or it must be an enum")


def build_field(name, sch, null=False):
    """this is the entry point for the module"""

    field_type, sch, null = rationalize_type(sch, null)

    if name == "id":
        if sch.get("type") != "string" and sch.get("format") != "uuid":
            raise ValueError("field with name id must be a UUID")
        return "UUIDField", dict(primary_key=True, default="uuid.uuid4")

    if field_type == "string":
        return build_string_field(sch, null)

    if field_type == "integer":
        validators = build_value_validators(sch)
        return "IntegerField", dict(null=null, validators=validators)

    if field_type == "number":
        validators = build_value_validators(sch)
        return "DecimalField", dict(null=null, validators=validators, max_digits=10, decimal_places=5)

    if field_type == "boolean":
        return "BooleanField", dict(null=null)

    raise NotImplementedError(f"no code written for type: {field_type}")


def build_relations(sch, null=False):
    field_type = sch.get("type")
    if field_type == "object":
        model = sch["$ref"].split("/")[-1]
        return model, null, False

    if field_type == "array":
        model = sch["array"][0]["$ref"].split("/")[-1]
        return model, null, True

    raise NotImplementedError(f"no code written for type: {field_type}")
