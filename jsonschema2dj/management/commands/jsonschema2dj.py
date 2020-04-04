from json import load
from django.core.management.base import BaseCommand

from jsonschema2dj.models import build_dependency_order, Model


VIEW_TEMPLATE = """
class {view_name}ViewSet(viewsets.ModelViewSet):
    queryset = models.{model_name}Model.objects.all()
    serializer_class = serializers.{model_name}Serializer
"""

URL_TEMPLATE = """
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

for name, obj in vars(views).items():
    if isinstance(obj, type):
        router.register(name, obj)

urlpatterns = [
    path("", include(router.urls)),
]
"""


class Command(BaseCommand):
    help: str = """blah blah blah
"""

    def add_arguments(self, parser):
        parser.add_argument("app", type=str, help="vnsknvcsl")

    def handle(self, *args, **kwargs) -> None:

        base_dir = kwargs["app"]

        with open(f"{base_dir}/schema.json") as f:
            schema = load(f)

        models, serializers, views = [], [], []

        for model_name in build_dependency_order(schema):
            model_schema = schema["definitions"][model_name]
            model = Model(model_name, model_schema)
            models.append(model.model_repr())
            serializers.append(model.serializer_repr())

        for view_name, model in schema["properties"].items():
            model_name = model["$ref"].split("/")[-1]
            views.append(
                VIEW_TEMPLATE.format(view_name=view_name, model_name=model_name)
            )

        with open(f"{base_dir}/models.py", "w") as f:
            f.write(
                "import uuid\nfrom django.core import validators\nfrom django.db import models\n\n"
                + "\n".join(models)
            )

        with open(f"{base_dir}/serializers.py", "w") as f:
            f.write(
                "from . import models\nfrom drf_writable_nested.serializers import WritableNestedModelSerializer\n\n"
                + "\n".join(serializers)
            )

        with open(f"{base_dir}/views.py", "w") as f:
            f.write(
                "from rest_framework import viewsets\nfrom . import serializers, models\n\n"
                + "\n".join(views)
            )

        with open(f"{base_dir}/urls.py", "w") as f:
            f.write(URL_TEMPLATE)
