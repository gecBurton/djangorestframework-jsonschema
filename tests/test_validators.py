import pytest
from django.core.exceptions import ValidationError

from jsonschema2dj.valdiators import JSONSchemaValidator

VALID_SCHEMAS = [
    (
        {"$ref": "#/definitions/abc"},
        {
            "abc": {
                "additionalProperties": False,
                "properties": {
                    "a": {"type": "integer"},
                    "b": {"type": "string"},
                    "c": {"type": "boolean"},
                },
            }
        },
        {"a": 1, "b": "hello", "c": False},
    ),
    ({"required": ["a"]}, None, {"a": 1},),
    (
        {
            "additionalProperties": False,
            "properties": {"c": {"type": "string", "pattern": "\\d+"}},
        },
        None,
        {"c": "123"},
    ),
]
INVALID_SCHEMAS = [
    (
        {"$ref": "#/definitions/abc"},
        {
            "abc": {
                "additionalPropertes": False,
                "properties": {
                    "a": {"type": "integer"},
                    "b": {"type": "string"},
                    "c": {"type": "boolean"},
                },
            }
        },
        {"a": 1.2, "b": True, "c": False},
        [
            "JSONSchema: 1.2 is not of type 'integer'",
            "JSONSchema: True is not of type 'string'",
        ],
    ),
    ({"required": ["a"]}, None, {"b": 1}, ["JSONSchema: 'a' is a required property"]),
    (
        {
            "additionalProperties": False,
            "properties": {"c": {"type": "string", "pattern": "\\d+"}},
        },
        None,
        {"b": 1, "c": "abc"},
        [
            "JSONSchema: Additional properties are not allowed ('b' was unexpected)",
            "JSONSchema: 'abc' does not match '\\d+'",
        ],
    ),
]


@pytest.mark.parametrize("schema,definitions,payload", VALID_SCHEMAS)
def test_doesnt_raises_error(schema, definitions, payload):
    validator = JSONSchemaValidator(schema, definitions)
    validator(payload)
    assert True


@pytest.mark.parametrize("schema,definitions,payload,error_messages", INVALID_SCHEMAS)
def test_raises_error(schema, definitions, payload, error_messages):
    validator = JSONSchemaValidator(schema, definitions)
    with pytest.raises(ValidationError) as error:
        validator(payload)

    assert error.value.messages == error_messages
