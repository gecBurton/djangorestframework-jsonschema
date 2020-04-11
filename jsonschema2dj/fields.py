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


def build_choices(enums, _type="string"):
    "helper function for enums to choices"
    if _type == "string":
        names = [value.lower().replace(" ", "_") for value in enums]
        return dict(max_length=max(map(len, enums)), choices=list(zip(names, enums)))

    if _type == "integer":
        return dict(choices=list(zip(map(str, enums), enums)))

    raise NotImplementedError("only integer or string enums are supported")


def build_string_field(sch, null, primary_key):
    "the string case is complex enough to have its own function"
    options = dict(null=null, primary_key=primary_key)
    validators = []

    max_length = sch.get("maxLength", 255)
    min_length = sch.get("minLength")

    options.update(max_length=max_length)

    if min_length:
        validators.append(("MinLengthValidator", min_length))

    if (min_length and max_length <= min_length) or max_length > 255:
        return "TextField", options

    if enums := sch.get("enum"):
        options.update(build_choices(enums))

    if pattern := sch.get("pattern"):
        validators.append(("RegexValidator", f'r"{pattern}"'))

    if validators:
        options.update(validators=validators)

    if _format := sch.get("format"):

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
            return formats[_format], dict(null=options["null"], primary_key=primary_key)
        except KeyError:
            raise NotImplementedError(f"no code written to handle format: {_format}")

    return "CharField", options


def rationalize_type(sch):
    """the type is problematic especially with regards to enums and null"""
    null = False
    if _type := sch.get("type"):
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

    if enums := sch.get("enum"):
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
        return _type, sch, null

    raise ValueError(f"either the type must be specified or it must be an enum")


def build_field(name, sch, required):
    """this is the entry point for the module"""

    primary_key = (name == required[0]) if required else False

    field_type, sch, null = rationalize_type(sch)

    if name == "id":
        if sch.get("type") != "string" and sch.get("format") != "uuid":
            raise ValueError("field with name id must be a UUID")
        return "UUIDField", dict(default="uuid.uuid4", primary_key=primary_key)

    if field_type == "string":
        return build_string_field(sch, null, primary_key)

    if field_type == "integer":
        validators = build_value_validators(sch)
        return (
            "IntegerField",
            dict(null=null, validators=validators, primary_key=primary_key),
        )

    if field_type == "number":
        validators = build_value_validators(sch)
        return (
            "DecimalField",
            dict(
                null=null,
                validators=validators,
                max_digits=10,
                decimal_places=5,
                primary_key=primary_key,
            ),
        )

    if field_type == "boolean":
        return "BooleanField", dict(null=null, primary_key=primary_key)

    raise NotImplementedError(f"no code written for type: {field_type}")


def build_relations(sch, null=False):
    if set(sch.keys()) == {
        "$ref",
    }:
        model = sch["$ref"].split("/")[-1]
        return model, null, False

    if sch.get("items"):
        model = sch["items"]["$ref"].split("/")[-1]
        return model, null, True

    raise NotImplementedError(f"no code written for type: {sch}")
