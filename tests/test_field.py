from json import load

import pytest

from jsonschema2dj.fields import build_field

with open("tests/schemas/single_fields.json") as f:
    single_fields = load(f)


results = {
    "basic": ("CharField", {"max_length": 255, "null": False, "primary_key": True}),
    "length": (
        "CharField",
        {
            "max_length": 3,
            "validators": [("MinLengthValidator", 2)],
            "null": False,
            "primary_key": False,
        },
    ),
    "regular_expressions": (
        "CharField",
        {
            "max_length": 255,
            "validators": [
                ("RegexValidator", 'r"^(\\([0-9]{3}\\))?[0-9]{3}-[0-9]{4}$"')
            ],
            "null": False,
            "primary_key": False,
        },
    ),
    "format_date-time": ("DateTimeField", {"null": False, "primary_key": False}),
    "format_time": ("TimeField", {"null": False, "primary_key": False}),
    "format_date": ("DateField", {"null": False, "primary_key": False}),
    "format_email": ("EmailField", {"null": False, "primary_key": False}),
    "format_idn-email": ("EmailField", {"null": False, "primary_key": False}),
    "format_ipv4": ("GenericIPAddressField", {"null": False, "primary_key": False}),
    "format_ipv6": ("GenericIPAddressField", {"null": False, "primary_key": False}),
    "boolean": ("BooleanField", {"null": False, "primary_key": False}),
    "integer": (
        "IntegerField",
        {"validators": [], "null": False, "primary_key": False},
    ),
    "enum": (
        "CharField",
        {
            "max_length": 1,
            "choices": [("a", "A"), ("b", "b"), ("c", "C")],
            "null": False,
            "primary_key": False,
        },
    ),
    "integer-minimum-maximum": (
        "IntegerField",
        {
            "validators": [("MinValueValidator", 3), ("MaxValueValidator", 5)],
            "null": False,
            "primary_key": False,
        },
    ),
    "enum-null": (
        "CharField",
        {
            "max_length": 1,
            "choices": [("a", "A"), ("b", "b"), ("c", "C")],
            "null": True,
            "primary_key": False,
        },
    ),
    "boolean-null": ("BooleanField", {"null": True, "primary_key": False}),
    "format-uuid": ("UUIDField", {"null": False, "primary_key": False}),
    "id": (
        "UUIDField",
        {"primary_key": True, "default": "uuid.uuid4", "primary_key": False},
    ),
    "json-schema": (
        "JSONSchemaField",
        {
            "schema": {
                "properties": {
                    "a": {"type": "boolean"},
                    "b": {"type": "integer"},
                    "c": {"type": "boolean"},
                },
                "required": ["a", "b"],
                "type": "object",
            }
        },
    ),
}


@pytest.mark.parametrize("name,result", results.items())
def test_build_field_pass(name, result):
    schema = single_fields["properties"][name]
    assert build_field(name, schema, single_fields.get("required", [])) == result


format_failures = [
    "format_hostname",
    "format_idn-hostname",
    "format_uri",
    "format_uri-reference",
    "format_iri",
    "format_iri-reference",
    "format_uri-template",
    "format_json-pointer",
    "format_relative-json-pointer",
    "format_regex",
]


@pytest.mark.parametrize("name", format_failures)
def test_build_field_fail_not_implemented(name):
    schema = single_fields["properties"][name]
    with pytest.raises(NotImplementedError):
        assert build_field(name, schema, single_fields.get("required", []))


type_errors = ["type-fail-empty", "type-fail-too-many", "type-fail-no-null"]


@pytest.mark.parametrize("name", type_errors)
def test_build_field_fail_types(name):
    schema = single_fields["properties"][name]
    with pytest.raises(ValueError):
        assert build_field(name, schema, single_fields.get("required", []))
