from collections import defaultdict
from json import load

import pytest

from jsonschema2dj.models import (
    build_dependency_order,
    Model,
    build_model_view,
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
    assert model.relations == relations


def test_build_dependency_order():
    assert build_dependency_order(simple_tree) == ["F", "D", "C", "E", "B", "A"]


def test_build_model_view_explicit():
    model_view = build_model_view(explicit_cardinalities)
    assert model_view == {'A': ({'B': 'b'}, {}),
                          'B': ({'A': 'a', 'C': 'c'}, {}),
                          'C': ({'D': 'd'}, {'B': 'b'}),
                          'D': ({}, {'C': 'c', 'E': 'e'}),
                          'E': ({}, {'D': 'd'})}

    x= build_relationships(model_view)
    assert x =={'A': {'m2m': {}, 'o2m': {}, 'o2o': {'b': 'B'}},
                'B': {'m2m': {}, 'o2m': {'c': 'C'}, 'o2o': {'a': 'A'}},
                'C': {'m2m': {}, 'o2m': {'d': 'D'}, 'o2o': {}},
                'D': {'m2m': {'e': 'E'}, 'o2m': {}, 'o2o': {}},
                'E': {'m2m': {'d': 'D'}, 'o2m': {}, 'o2o': {}}}


def test_build_model_view_implicit():
    model_view = build_model_view(implicit_cardinalities)
    assert model_view == {'A': ({'B': 'b'}, {}),
                          'B': ({'A': 'a', 'C': 'c'}, {}),
                          'C': ({'D': 'd'}, {}),
                          'D': ({}, {'E': 'e'}),
                          'E': ({}, {})}

    x= build_relationships(model_view)
    assert x =={'A': {'m2m': {}, 'o2m': {}, 'o2o': {'b': 'B'}},
                'B': {'m2m': {}, 'o2m': {'c': 'C'}, 'o2o': {'a': 'A'}},
                'C': {'m2m': {}, 'o2m': {'d': 'D'}, 'o2o': {}},
                'D': {'m2m': {'e': 'E'}, 'o2m': {}, 'o2o': {}},
                'E': {'m2m': {}, 'o2m': {}, 'o2o': {}}}


def test_build_():
    model_view = build_model_view(simple_tree)
    assert model_view == {'A': ({'B': 'b'}, {}),
                          'B': ({'C': 'c', 'E': 'e'}, {}),
                          'C': ({'D': 'd'}, {}),
                          'D': ({}, {}),
                          'E': ({'F': 'f'}, {}),
                          'F': ({}, {})}

    x= build_relationships(model_view)
    assert x == {'A': {'m2m': {}, 'o2m': {'b': 'B'}, 'o2o': {}},
                 'B': {'m2m': {}, 'o2m': {'c': 'C', 'e': 'E'}, 'o2o': {}},
                 'C': {'m2m': {}, 'o2m': {'d': 'D'}, 'o2o': {}},
                 'D': {'m2m': {}, 'o2m': {}, 'o2o': {}},
                 'E': {'m2m': {}, 'o2m': {'f': 'F'}, 'o2o': {}},
                 'F': {'m2m': {}, 'o2m': {}, 'o2o': {}}}











