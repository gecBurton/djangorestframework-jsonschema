import pytest

from jsonschema2dj.relationships import extract_relationships, build_models
from tests.test_schema import tuple_to_list


SCHEMAS = [
    (
        "None-to-None",
        {"A": {}, "B": {}},
        {'A': ({}, {}, {}), 'B': ({}, {}, {})},
        {'A': [], 'B': []}
    ),
    (
        "None-to-One",
        {"A": {}, "B": {"a": {"$ref": "#/definitions/A"}}},
        {'A': ({}, {}, {}), 'B': ({'A': ('a', True)}, {}, {})},
        {'A': [], 'B': [{'null': True, 'to': 'A', 'type': 'ForeignKey'}]}
    ),
    (
        "One-to-None",
        {"A": {"b": {"$ref": "#/definitions/B"}}, "B": {}},
        {'A': ({'B': ('b', True)}, {}, {}), 'B': ({}, {}, {})},
        {'A': [{'null': True, 'to': 'B', 'type': 'ForeignKey'}], 'B': []}
    ),
    (
        "None-to-Many",
        {"A": {}, "B": {"a": {"items": {"$ref": "#/definitions/A"}}}},
        {'A': ({}, {}, {}), 'B': ({}, {'A': ('a', True)}, {})},
        {'A': [], 'B': [{'null': True, 'to': 'A', 'type': 'ManyToManyField'}]}
    ),
    (
        "Many-to-None",
        {"A": {"b": {"items": {"$ref": "#/definitions/B"}}}, "B": {}},
        {'A': ({}, {'B': ('b', True)}, {}), 'B': ({}, {}, {})},
        {'A': [{'null': True, 'to': 'B', 'type': 'ManyToManyField'}], 'B': []}
    ),
    (
        "One-to-One",
        {"A": {"b": {"$ref": "#/definitions/B"}}, "B": {"a": {"$ref": "#/definitions/A"}}},
        {'A': ({'B': ('b', True)}, {}, {}), 'B': ({'A': ('a', True)}, {}, {})},
        {
            'A': [{'null': True, 'to': 'B', 'type': 'OneToOneField'}],
            'B': [{'null': True, 'to': 'A', 'type': 'OneToOneField'}]
        }
    ),
    (
        "One-to-Many",
        {"A": {"b": {"$ref": "#/definitions/B"}}, "B": {"a": {"items": {"$ref": "#/definitions/A"}}}},
        {'A': ({'B': ('b', True)}, {}, {}), 'B': ({}, {'A': ('a', True)}, {})},
        {
            'A': [{'null': True, 'to': 'B', 'type': 'ForeignKey'}],
            'B': []
        }
    ),
    (
        "Many-to-One",
        {"A": {"b": {"items": {"$ref": "#/definitions/B"}}}, "B": {"a": {"$ref": "#/definitions/A"}}},
        {'A': ({}, {'B': ('b', True)}, {}), 'B': ({'A': ('a', True)}, {}, {})},
        {
            'A': [],
            'B': [{'null': True, 'to': 'A', 'type': 'ForeignKey'}]
        }
    ),
    (
        "Many-to-Many",
        {"A": {"b": {"items": {"$ref": "#/definitions/B"}}}, "B": {"a": {"items": {"$ref": "#/definitions/A"}}}},
        {'A': ({}, {'B': ('b', True)}, {}), 'B': ({}, {'A': ('a', True)}, {})},
        {
            'A': [{'null': True, 'to': 'B', 'type': 'ManyToManyField'}],
            'B': [{'null': True, 'to': 'A', 'type': 'ManyToManyField'}]
        }
    ),
]


@pytest.mark.parametrize("name, reduced_schema, expected_relationships, expected_models", SCHEMAS)
def test_relationships(name, reduced_schema, expected_relationships, expected_models):
    schema = {
        "properties": {
            model: {
                "properties": fields
            }
            for model, fields in reduced_schema.items()
        }
    }

    relationships = extract_relationships(schema)

    assert extract_relationships(schema) == expected_relationships

    assert tuple_to_list(build_models(relationships)) == expected_models
