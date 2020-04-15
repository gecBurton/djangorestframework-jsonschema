from json import load

import pytest

from jsonschema2dj.models import (
    Model,
    build_relationships,
)

with open("tests/schemas/basic_model.json") as f:
    basic_model = load(f)

with open("tests/schemas/simple_tree.json") as f:
    simple_tree = load(f)

with open("tests/schemas/explicit_cardinalities.json") as f:
    explicit_cardinalities = load(f)

with open("tests/schemas/implicit_cardinalities.json") as f:
    implicit_cardinalities = load(f)

with open("tests/schemas/simple_tree.json") as f:
    simple_tree = load(f)


results = {
    "person": (
        "person",
        {
            "age": (
                "IntegerField",
                {
                    "null": False,
                    "primary_key": False,
                    "validators": [("MinValueValidator", 0)],
                },
            ),
            "id": ("UUIDField", {"primary_key": True, "default": "uuid.uuid4"}),
            "name": (
                "CharField",
                {"max_length": 255, "null": False, "primary_key": False},
            ),
            "sex": (
                "CharField",
                {
                    "choices": [("male", "male"), ("female", "female")],
                    "max_length": 6,
                    "null": True,
                    "primary_key": False,
                },
            ),
        },
        ["sex"],
    )
}


@pytest.mark.parametrize("name,result", results.items())
def test_build_model_pass(name, result):
    schema = basic_model["definitions"][name]
    model = Model(name, schema)
    name, fields, enums = result
    assert model.name == name
    assert model.fields == fields
    assert model.enums == enums


results = [
    ("A", {}, [], {"b": ("B", True, False)}),
    ("B", {}, [], {"c": ("C", True, False), "e": ("E", True, False)}),
    ("C", {}, [], {"d": ("D", True, False)}),
    ("D", {}, [], {}),
    ("E", {}, [], {"f": ("F", True, False)}),
    ("F", {}, [], {}),
]


@pytest.mark.parametrize("name,fields,enums,relations", results)
def test_build_model_tree_pass(name, fields, enums, relations):
    schema = simple_tree["definitions"][name]
    model = Model(name, schema)
    assert model.name == name
    assert model.fields == fields
    assert model.enums == enums



def test_build_model_view_explicit():

    x= build_relationships(explicit_cardinalities)
    assert x =={'A': {'m2m': {}, 'o2m': {}, 'o2o': {'b': 'B'}},
                'B': {'m2m': {}, 'o2m': {'c': 'C'}, 'o2o': {'a': 'A'}},
                'C': {'m2m': {}, 'o2m': {'d': 'D'}, 'o2o': {}},
                'D': {'m2m': {'e': 'E'}, 'o2m': {}, 'o2o': {}},
                'E': {'m2m': {'d': 'D'}, 'o2m': {}, 'o2o': {}}}


def test_build_model_view_implicit():

    x= build_relationships(implicit_cardinalities)
    assert x =={'A': {'m2m': {}, 'o2m': {}, 'o2o': {'b': 'B'}},
                'B': {'m2m': {}, 'o2m': {'c': 'C'}, 'o2o': {'a': 'A'}},
                'C': {'m2m': {}, 'o2m': {'d': 'D'}, 'o2o': {}},
                'D': {'m2m': {'e': 'E'}, 'o2m': {}, 'o2o': {}},
                'E': {'m2m': {}, 'o2m': {}, 'o2o': {}}}


def test_build_():

    x= build_relationships(simple_tree)
    assert x == {'A': {'m2m': {}, 'o2m': {'b': 'B'}, 'o2o': {}},
                 'B': {'m2m': {}, 'o2m': {'c': 'C', 'e': 'E'}, 'o2o': {}},
                 'C': {'m2m': {}, 'o2m': {'d': 'D'}, 'o2o': {}},
                 'D': {'m2m': {}, 'o2m': {}, 'o2o': {}},
                 'E': {'m2m': {}, 'o2m': {'f': 'F'}, 'o2o': {}},
                 'F': {'m2m': {}, 'o2m': {}, 'o2o': {}}}











