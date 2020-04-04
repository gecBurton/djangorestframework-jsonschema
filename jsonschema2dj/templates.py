from typing import List

from jinja2 import Template

from jsonschema2dj.models import Model

VIEW_TEMPLATE = """
from rest_framework import viewsets
from . import serializers, models

{% for view_name, model_name in views %}
class {{view_name}}ViewSet(viewsets.ModelViewSet):
    queryset = models.{{model_name}}Model.objects.all()
    serializer_class = serializers.{{model_name}}Serializer

{% endfor %}
"""

SERIALIZER_TEMPLATE = """
from . import models
from drf_writable_nested.serializers import WritableNestedModelSerializer


{% for model in models %}
class {{model.name}}Serializer(WritableNestedModelSerializer):
{% for serializer in model.serializers %}
    {{serializer.name}} = {{serializer.model}}Serializer()
{% endfor %}

    class Meta:
        model = models.{{model.name}}Model
        fields = '__all__'

{% endfor %}
"""

MODEL_TEMPLATE = """
import uuid
from django.core import validators
from django.db import models

{% for model in models %}
class {{model.name}}Model(models.Model):
{% for name, (type, options) in model.fields_str.items() %}
    {{name}} = models.{{type}}({{options}})
{% endfor %}

{% for name, (type, null, many) in model.relations.items() %}
    {{name}} = models.ForeignKey({{type}}Model, null={{null}}, on_delete=models.CASCADE)
{% endfor %}

{% endfor %}
"""

URL_TEMPLATE = """
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

{% for view_name, model_name in views %}
router.register("{{view_name}}", views.{{model_name}}ViewSet)
{% endfor %}

urlpatterns = [
    path("", include(router.urls)),
]
"""


def build_models(models: List[Model]) -> str:
    return Template(MODEL_TEMPLATE).render(models=models)


def build_serializers(models: List[Model]) -> str:
    return Template(SERIALIZER_TEMPLATE).render(models=models)


def build_views(views: List[Model]) -> str:
    return Template(VIEW_TEMPLATE).render(views=views)


def build_urls(views: List[Model]) -> str:
    return Template(URL_TEMPLATE).render(views=views)
