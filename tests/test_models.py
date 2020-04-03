from json import load

import pytest

from jsonschema2dj.models import build_model, build_dependency_order

with open("tests/schemas/basic_model.json") as f:
    basic_model = load(f)

with open("tests/schemas/simple_tree.json") as f:
    simple_tree = load(f)

results = {
    "person": (
        "person",
        {
            "age": (
                "IntegerField",
                {"null": False, "validators": [("MinValueValidator", 0)]},
            ),
            "id": ("UUIDField", {"primary_key": True, "default": "uuid.uuid4"}),
            "name": ("CharField", {"max_length": 255, "null": False}),
            "sex": (
                "CharField",
                {
                    "choices": [("male", "male"), ("female", "female")],
                    "max_length": 6,
                    "null": True,
                },
            ),
        },
    )
}


@pytest.mark.parametrize("name,result", results.items())
def test_build_model_pass(name, result):
    schema = basic_model["definitions"][name]
    assert build_model(name, schema), {} == result


def test_build_dependency_order():
    assert build_dependency_order(simple_tree) == ['F', 'D', 'C', 'E', 'B', 'A']
