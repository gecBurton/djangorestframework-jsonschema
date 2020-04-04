from json import load
from django.core.management.base import BaseCommand

from jsonschema2dj.models import build_dependency_order, Model
from jsonschema2dj.templates import (
    build_models,
    build_serializers,
    build_views,
    build_urls,
)


class Command(BaseCommand):
    help: str = "blah blah blah"

    def add_arguments(self, parser):
        parser.add_argument("app", type=str, help="vnsknvcsl")

    def handle(self, *args, **kwargs) -> None:

        base_dir = kwargs["app"]

        with open(f"{base_dir}/schema.json") as f:
            schema = load(f)

        models = [
            Model(model_name, schema["definitions"][model_name])
            for model_name in build_dependency_order(schema)
        ]
        views = [(a, b["$ref"].split("/")[-1]) for a, b in schema["properties"].items()]

        with open(f"{base_dir}/models.py", "w") as f:
            f.write(build_models(models=models))

        with open(f"{base_dir}/serializers.py", "w") as f:
            f.write(build_serializers(models=models))

        with open(f"{base_dir}/views.py", "w") as f:
            f.write(build_views(views=views))

        with open(f"{base_dir}/urls.py", "w") as f:
            f.write(build_urls(views=views))
