from json import load

import pytest

from jsonschema2dj.models import (
    Model,
    build_relationships,
)

with open("tests/json-schemas/basic_model.json") as f:
    basic_model = load(f)

with open("tests/json-schemas/simple_tree.json") as f:
    simple_tree = load(f)

with open("tests/json-schemas/explicit_cardinalities.json") as f:
    explicit_cardinalities = load(f)

with open("tests/json-schemas/implicit_cardinalities.json") as f:
    implicit_cardinalities = load(f)

with open("tests/json-schemas/simple_tree.json") as f:
    simple_tree = load(f)


results = {
    "person": (
        "person",
        {
            "age":                 {
                    "type":         "IntegerField",
                    "null": False,
                    "primary_key": False,
                    "validators": "[validators.MinValueValidator(0)]",
                },

            "id": {"type":"UUIDField", "primary_key": True, "default": "uuid.uuid4"},
            "name": {"type":
                "CharField",
                "max_length": 255, "null": False, "primary_key": False},

            "sex": {"type":
                "CharField",

                    "choices": [("male", "male"), ("female", "female")],
                    "max_length": 6,
                    "null": True,
                    "primary_key": False,
                },

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
    assert model.enum_fields == enums


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
    assert model.enum_fields == enums


def test_build_model_view_explicit():

    x = build_relationships(explicit_cardinalities)
    assert x == {
        "A": {
            "b": {"type":"OneToOneField", "to": "B", "null": True, "on_delete": "models.CASCADE"}
        },
        "B": {
            "a": {"type":"OneToOneField", "to": "A", "null": True, "on_delete": "models.CASCADE"},
            "c": {"type":"ForeignKey", "to":"C", "null": True, "on_delete": "models.CASCADE"},
        },
        "C": {"d": {"type":"ForeignKey", "to":"D", "null": True, "on_delete": "models.CASCADE"}},
        "D": {
            "e": {"type":"ManyToManyField", "to":"E", "null": True, "on_delete": "models.CASCADE"}
        },
        "E": {
            "d": {"type":"ManyToManyField", "to":"D", "null": True, "on_delete": "models.CASCADE"}
        },
    }


def test_build_model_view_implicit():

    x = build_relationships(implicit_cardinalities)
    assert x == {
        "A": {
            "b": {"type":"OneToOneField", "to":"B", "null": True, "on_delete": "models.CASCADE"}
        },
        "B": {
            "a": {"type":"OneToOneField", "to":"A", "null": True, "on_delete": "models.CASCADE"},
            "c": {"type":"ForeignKey", "to":"C", "null": True, "on_delete": "models.CASCADE"},
        },
        "C": {"d": {"type":"ForeignKey", "to":"D", "null": True, "on_delete": "models.CASCADE"}},
        "D": {
            "e": {"type":"ManyToManyField", "to":"E", "null": True, "on_delete": "models.CASCADE"}
        },
        "E": {},
    }


def test_build_():

    x = build_relationships(simple_tree)
    assert x == {
        "A": {"b": {"type":"ForeignKey", "to":"B", "null": True, "on_delete": "models.CASCADE"}},
        "B": {
            "c": {"type":"ForeignKey", "to":"C", "null": True, "on_delete": "models.CASCADE"},
            "e": {"type":"ForeignKey", "to":"E", "null": True, "on_delete": "models.CASCADE"},
        },
        "C": {"d": {"type":"ForeignKey","to": "D", "null": True, "on_delete": "models.CASCADE"}},
        "D": {},
        "E": {"f": {"type":"ForeignKey", "to": "F", "null": True, "on_delete": "models.CASCADE"}},
        "F": {},
    }
