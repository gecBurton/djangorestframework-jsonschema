from json import load

import pytest

from jsonschema2dj.fields import build_field

with open("tests/single_fields.json") as f:
    single_fields = load(f)


results = {
    "basic": {
        "type": "CharField",
        "max_length": 255,
        "primary_key": True,
    },
    "length": {
        "type": "CharField",
        "max_length": 3,
        "validators": {"MinLengthValidator": 2},
    },
    "regular_expressions": {
        "type": "CharField",
        "max_length": 255,
        "validators": {"RegexValidator": "^(\\([0-9]{3}\\))?[0-9]{3}-[0-9]{4}$"},
    },
    "format_date-time": {"type": "DateTimeField"},
    "format_time": {"type": "TimeField"},
    "format_date": {"type": "DateField"},
    "format_email": {"type": "EmailField"},
    "format_idn-email": {"type": "EmailField"},
    "format_ipv4": {
        "type": "GenericIPAddressField",
    },
    "format_ipv6": {
        "type": "GenericIPAddressField",
    },
    "boolean": {"type": "BooleanField"},
    "integer": {
        "default": 2,
        "type": "IntegerField",
        "validators": {},
    },
    "enum": {
        "type": "CharField",
        "max_length": 1,
        "choices": [("a", "A"), ("b", "b"), ("c", "C")],
    },
    "integer-minimum-maximum": {
        "type": "IntegerField",
        "validators": {"MinValueValidator": 3, "MaxValueValidator": 5},
    },
    "enum-null": {
        "type": "CharField",
        "max_length": 1,
        "choices": [("a", "A"), ("b", "b"), ("c", "C")],
        "null": True
    },
    "boolean-null": {"type": "BooleanField",  "null": True},
    "format-uuid": {"type": "UUIDField",  "default": "uuid.uuid4"},
    "id": {
        "type": "UUIDField",
        "default": "uuid.uuid4",
    },
    "json-schema":
        {'type': 'JSONField',
         'validators': {'JSONSchemaValidator': {'properties': {'a': {'type': 'boolean'},
                                                               'b': {'type': 'integer'},
                                                               'c': {'type': 'boolean'}},
                                                'required': ['a', 'b'],
                                                'type': 'object'}}}
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
