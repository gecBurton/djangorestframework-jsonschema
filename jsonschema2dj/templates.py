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
from rest_framework.serializers import ModelSerializer


{% for model in models %}
class {{model.name}}Serializer(ModelSerializer):
{% for name, (model, null, many) in model.relations.items() %}
    {{name}} = {{model}}Serializer(allow_null={{null}}, many={{many}})
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

ADMIN_TEMPLATE = """
from django.contrib import admin
from . import models

{% for model in models %}
@admin.register(models.{{model.name}}Model)
class {{model.name}}Admin(admin.ModelAdmin):
    list_filter = (
{% for enum in model.enums %}
        "{{enum}}",
{% endfor %}
    )
{% endfor %}
"""


def build_models(models: List[Model]) -> str:
    return Template(MODEL_TEMPLATE).render(models=models)


def build_serializers(models: List[Model]) -> str:
    return Template(SERIALIZER_TEMPLATE).render(models=models)


def build_admin(models: List[Model]) -> str:
    return Template(ADMIN_TEMPLATE).render(models=models)


def build_views(views: List[Model]) -> str:
    return Template(VIEW_TEMPLATE).render(views=views)


def build_urls(views: List[Model]) -> str:
    return Template(URL_TEMPLATE).render(views=views)
