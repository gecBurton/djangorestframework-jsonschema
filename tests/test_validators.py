import pytest
from django.core.exceptions import ValidationError

from jsonschema2dj.valdiators import JSONSchemaValidator

VALID_SCHEMAS = [
    ({"required": ["a"]}, {"a": 1}),
    (
        {
            "additionalProperties": False,
            "properties": {"c": {"type": "string", "pattern": "\d+"}},
        },
        {"c": "123"},
    ),
]
INVALID_SCHEMAS = [
    ({"required": ["a"]}, {"b": 1}, ["JSONSchema: 'a' is a required property"]),
    (
        {
            "additionalProperties": False,
            "properties": {"c": {"type": "string", "pattern": "\d+"}},
        },
        {"b": 1, "c": "abc"},
        [
            "JSONSchema: Additional properties are not allowed ('b' was unexpected)",
            "JSONSchema: 'abc' does not match '\\d+'",
        ],
    ),
]


@pytest.mark.parametrize("schema,payload", VALID_SCHEMAS)
def test_raises_error(schema, payload):
    validator = JSONSchemaValidator(schema)
    validator(payload)
    assert True


@pytest.mark.parametrize("schema,payload,error_messages", INVALID_SCHEMAS)
def test_raises_error(schema, payload, error_messages):
    validator = JSONSchemaValidator(schema)
    with pytest.raises(ValidationError) as error:
        validator(payload)

    assert error.value.messages == error_messages
