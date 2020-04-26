import os
from json import load

import pytest

from jsonschema2dj.models import Model, build_models, Dependent

json_schema_dir = "tests/json-schemas/"
django_schema_dir = "tests/django-schemas/"


schemas = zip(os.listdir(json_schema_dir), os.listdir(django_schema_dir))


def tuple_to_list(obj):
    if isinstance(obj, dict):
        return {k: tuple_to_list(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return list(map(tuple_to_list, obj))
    return obj


@pytest.mark.parametrize("json_file, django_file", schemas)
def test_django_schema(json_file, django_file):
    with open(json_schema_dir + json_file) as f:
        json_schema = load(f)

    with open(django_schema_dir + django_file) as f:
        django_schema = load(f)

    assert [
        tuple_to_list(m.dict_repr) for m in Model.factory(json_schema)
    ] == django_schema


# trees = [
#     {'A': [], 'B': ['C'], 'C': ['D'], 'D': [], 'E': []},
#     {'ResponsibleClinician': [],
#      'manifest': ['plate'],
#      'plate': [],
#      'redcap': ['ResponsibleClinician']},
#     {'A': [], 'B': ['C'], 'C': ['D'], 'D': [], 'E': []},
#     {'A': ['B'], 'B': ['C', 'E'], 'C': ['D'], 'D': [], 'E': ['F'], 'F': []},
#     {'person': []},
#     {'Doctor': ['Hospital'], 'Hospital': [], 'Patient': []},
# ]
# models = zip(os.listdir(json_schema_dir), trees)
#
#
#
# eg = {'A': ['B'], 'B': ['C', 'E'], 'C': ['D'], 'D': [], 'E': ['F'], 'F': []}
#
#
# @pytest.mark.parametrize("json_file, tree", models)
# def test_build_models(json_file, tree):
#     with open(json_schema_dir + json_file) as f:
#         json_schema = load(f)
#
#     m = Dependent.sort_models(build_models(json_schema))
#     assert m == tree
#
#
