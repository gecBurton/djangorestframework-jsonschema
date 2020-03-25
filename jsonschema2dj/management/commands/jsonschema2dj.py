from json import load
from django.core.management.base import BaseCommand
from django.core.management.color import no_style

from jsonschema2dj.models import build_model

MODEL_TEMPLATE = """
class {name}Model(models.Model):

{fields}
{relations}

"""

FIELD_TEMPLATE = "    {name} = models.{field_type}({options})"


SERIALIZER_TEMPLATE = """
class {name}Serializer(WritableNestedModelSerializer):
{serializers}
    class Meta:
        model = models.{name}Model
        fields = '__all__'
"""

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
        parser.add_argument('app', type=str, help="vnsknvcsl")

    def handle(self, *args, **kwargs) -> None:

        base_dir = kwargs["app"]

        with open(f"{base_dir}/schema.json") as f:
            schema = load(f)

        models, serializers, views = [], [], []
        for model_name, model_schema in schema["definitions"].items():
            _, fields, relations = build_model(model_name, model_schema)
            field_strs = []
            rels_strs = []
            serializer_strs = []
            for field_name, (field_type, field_attrs) in fields.items():
                validators = field_attrs.get("validators")
                if validators:
                    field_attrs["validators"] = (
                        "[" + ", ".join(f"validators.{a}({b})" for a, b in validators) + "]"
                    )
                field_attrs_dict = ", ".join(
                    f"{k}={v}".format(k, v) for k, v in field_attrs.items()
                )
                field_strs.append(
                    FIELD_TEMPLATE.format(
                        name=field_name, field_type=field_type, options=field_attrs_dict
                    )
                )

            for field_name, (model, null, many) in relations.items():
                rels_strs.append(f"    {field_name} = models.ForeignKey({model}Model, null={null}, many={many}, on_delete=models.CASCADE)")
                serializer_strs.append(f"    {field_name} = {model}Serializer()")

            models.append(MODEL_TEMPLATE.format(name=model_name, fields="\n".join(field_strs), relations="\n".join(rels_strs)))
            serializers.append(SERIALIZER_TEMPLATE.format(name=model_name, serializers="\n".join(serializer_strs)))

        for view_name, model in schema['properties'].items():
            model_name = model["$ref"].split('/')[-1]
            views.append(VIEW_TEMPLATE.format(view_name=view_name, model_name=model_name))

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
