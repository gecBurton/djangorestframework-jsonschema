import os
from json import load

import pytest

from jsonschema2dj.fields import Relationship, Field
from jsonschema2dj.models import Model

json_schema_dir = "tests/json-schemas/"
django_schema_dir = "tests/django-schemas/"


schemas = zip(os.listdir(json_schema_dir), os.listdir(django_schema_dir))


def tuple_to_list(obj):
    if isinstance(obj, dict):
        return {k: tuple_to_list(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return list(map(tuple_to_list, obj))
    if isinstance(obj, Relationship):
        return {**obj.options, "to": obj.to, "type": obj.type}
    if isinstance(obj, Field):
        return obj.options
    return obj


@pytest.mark.parametrize("json_file, django_file", schemas)
def test_django_schema(json_file, django_file):
    with open(json_schema_dir + json_file) as f:
        json_schema = load(f)

    with open(django_schema_dir + django_file) as f:
        django_schema = load(f)

    expected = []
    for model in Model.factory(json_schema):
        expected_model = dict(
            name=model.name,
            fields=[
                dict(
                    name=field.name,
                    type=field.type,
                    to=getattr(field, "to", None),
                    options=tuple_to_list(field.options)
                ) for field in model.fields
            ]
        )
        expected.append(expected_model)

    assert expected == django_schema
