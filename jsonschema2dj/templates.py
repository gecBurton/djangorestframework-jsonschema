from typing import List

from jinja2 import Template

from jsonschema2dj.models import Model

VIEW_TEMPLATE = """
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from . import serializers, models, filters

{% for model in models %}

class {{model.name}}(viewsets.ModelViewSet):
    queryset = models.{{model.name}}.objects.all()
    serializer_class = serializers.{{model.name}}
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.{{model.name}}
    ordering_fields = "__all__"
    search_fields = [
{% for field in model.search_fields %}
        "${{field}}",
{% endfor %}
    ]


{% endfor %}
"""

SERIALIZER_TEMPLATE = """
from . import models
from rest_framework.serializers import ModelSerializer


{% for model in models %}

class {{model.name}}(ModelSerializer):

    class Meta:
        model = models.{{model.name}}
        fields = '__all__'

{% endfor %}
"""

MODEL_TEMPLATE = """
import uuid
from django.core import validators
from django.db import models

{% for model in models %}

class {{model.name}}(models.Model):
{% for name, (type, options) in model.fields_str.items() %}
    {{name}} = models.{{type}}({{options}})
{% endfor %}

{% for name, model in model.o2o.items() %}
    {{name}} = models.OneToOneField({{model}}, null=True, on_delete=models.CASCADE)
{% endfor %}
{% for name, model in model.o2m.items() %}
    {{name}} = models.ForeignKey({{model}}, null=True, on_delete=models.CASCADE)
{% endfor %}
{% for name, model in model.m2m.items() %}
    {{name}} = models.ManyToManyField({{model}})
{% endfor %}

{% endfor %}
"""

URL_TEMPLATE = """
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

{% for model in models %}
router.register("{{model.name}}", views.{{model.name}})
{% endfor %}

urlpatterns = [
    path("", include(router.urls)),
]
"""

ADMIN_TEMPLATE = """
from django.contrib import admin
from . import models

{% for model in models %}

@admin.register(models.{{model.name}})
class {{model.name}}Admin(admin.ModelAdmin):
    list_filter = (
{% for enum in model.enums %}
        "{{enum}}",
{% endfor %}
    )
{% endfor %}
"""

FILTER_TEMPLATE = """
from django_filters import rest_framework as filters
from . import models

{% for model in models%}
class {{model.name}}(filters.FilterSet):
    class Meta:
        model = models.{{model.name}}
        fields = {
{% for name, (type, options) in model.fields.items() %}
{% if type in ("IntegerField", "DecimalField") %}
            "{{name}}": ["exact", "gte", "lte"],
{% elif "choices" in options.keys() %}
            "{{name}}": ["exact", "in"],
{% endif %}
{% endfor %}
            }


{% endfor %}

"""


def build_models(models: List[Model]) -> str:
    return Template(MODEL_TEMPLATE, trim_blocks=True).render(models=models)


def build_serializers(models: List[Model]) -> str:
    return Template(SERIALIZER_TEMPLATE, trim_blocks=True).render(models=models)


def build_admin(models: List[Model]) -> str:
    return Template(ADMIN_TEMPLATE, trim_blocks=True).render(models=models)


def build_views(models: List[Model]) -> str:
    return Template(VIEW_TEMPLATE, trim_blocks=True).render(models=models)


def build_urls(models: List[Model]) -> str:
    return Template(URL_TEMPLATE, trim_blocks=True).render(models=models)


def build_filters(models: List[Model]) -> str:
    return Template(FILTER_TEMPLATE, trim_blocks=True).render(models=models)
