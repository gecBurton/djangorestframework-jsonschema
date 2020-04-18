from json import load
from os import listdir, path

import pytest

from jsonschema2dj.models import Model
from jsonschema2dj.templates import (
    build_models,
    build_serializers,
    build_admin,
    build_views,
    build_urls,
    build_filters,
)


json_schema_dir = path.join("tests", "json-schemas")
django_files_dir = path.join("tests", "django-files")


assets = [
    ("admin", build_admin),
    ("filters", build_filters),
    ("models", build_models),
    ("serializers", build_serializers),
    ("urls", build_urls),
    ("views", build_views),
]

stuff = [
    (model, asset_name, asset_function)
    for asset_name, asset_function in assets
    for model in listdir(json_schema_dir)
]


@pytest.mark.parametrize("model,asset_name,asset_function", stuff)
def test_q(model, asset_name, asset_function):
    with open(path.join(json_schema_dir, model)) as f:
        schema = load(f)

    with open(
        path.join(django_files_dir, model.replace(".json", ""), asset_name + ".py")
    ) as f:
        model_file = f.read()

    assert asset_function(models=Model.factory(schema)) == model_file
