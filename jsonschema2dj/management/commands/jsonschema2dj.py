from json import load
from django.core.management.base import BaseCommand  # type: ignore

from jsonschema2dj.models import Model
from jsonschema2dj.templates import (
    build_models,
    build_serializers,
    build_views,
    build_urls,
    build_admin,
    build_filters,
)


class Command(BaseCommand):
    help = ""

    def add_arguments(self, parser):
        parser.add_argument("app", type=str, help="")

    def handle(self, *args, **kwargs) -> None:

        base_dir = kwargs["app"]

        with open(f"{base_dir}/schema.json") as f:
            schema = load(f)

        models = Model.factory(schema)

        with open(f"{base_dir}/models.py", "w") as f:
            f.write(build_models(models=models))

        with open(f"{base_dir}/serializers.py", "w") as f:
            f.write(build_serializers(models=models))

        with open(f"{base_dir}/admin.py", "w") as f:
            f.write(build_admin(models=models))

        with open(f"{base_dir}/views.py", "w") as f:
            f.write(build_views(models=models))

        with open(f"{base_dir}/urls.py", "w") as f:
            f.write(build_urls(models=models))

        with open(f"{base_dir}/filters.py", "w") as f:
            f.write(build_filters(models=models))
