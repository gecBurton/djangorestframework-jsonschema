from json import load

import pytest

from jsonschema2dj.fields import build_field

with open("tests/single_fields.json") as f:
    single_fields = load(f)


results = {
    "basic":  {"type":"CharField","max_length": 255, "null": False, "primary_key": True},
    "length":         {"type":         "CharField",

         "max_length": 3,
            "validators": [("MinLengthValidator", 2)],
            "null": False,
            "primary_key": False,
        },
    "regular_expressions":

        {
            "type":"CharField",
            "max_length": 255,
            "validators": [
                ("RegexValidator", 'r"^(\\([0-9]{3}\\))?[0-9]{3}-[0-9]{4}$"')
            ],
            "null": False,
            "primary_key": False,
        },

    "format_date-time": {"type": "DateTimeField","null": False, "primary_key": False},
    "format_time": {"type": "TimeField","null": False, "primary_key": False},
    "format_date": {"type": "DateField", "null": False, "primary_key": False},
    "format_email": {"type": "EmailField", "null": False, "primary_key": False},
    "format_idn-email": {"type": "EmailField", "null": False, "primary_key": False},
    "format_ipv4": {"type": "GenericIPAddressField", "null": False, "primary_key": False},
    "format_ipv6": {"type": "GenericIPAddressField", "null": False, "primary_key": False},
    "boolean": {"type": "BooleanField", "null": False, "primary_key": False},
    "integer": {"type":
        "IntegerField",
        "validators": "[]", "null": False, "primary_key": False}
    ,
    "enum": {"type":
        "CharField",

            "max_length": 1,
            "choices": [("a", "A"), ("b", "b"), ("c", "C")],
            "null": False,
            "primary_key": False,
        },
    "integer-minimum-maximum": {"type":
        "IntegerField",
            "validators": "[validators.MinValueValidator(3), validators.MaxValueValidator(5)]",
            "null": False,
            "primary_key": False,
        },
    "enum-null": {"type":
        "CharField",
            "max_length": 1,
            "choices": [("a", "A"), ("b", "b"), ("c", "C")],
            "null": True,
            "primary_key": False,
        },
    "boolean-null": {"type": "BooleanField", "null": True, "primary_key": False},
    "format-uuid": {"type": "UUIDField", "null": False, "primary_key": False},
    "id": {"type":
        "UUIDField",
        "primary_key": True, "default": "uuid.uuid4", "primary_key": False},

    "json-schema":
        {"type": "JSONSchemaField",

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
