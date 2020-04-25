from typing import List

from jinja2 import Template

from jsonschema2dj.models import Model

VIEW_TEMPLATE = """from rest_framework import viewsets
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
{% if model.search_fields|length %}
    search_fields = [
{% for field in model.search_fields %}
        "${{field}}",
{% endfor %}
    ]
{% endif %}
{% endfor %}
"""

SERIALIZER_TEMPLATE = """from . import models
from rest_framework.serializers import HyperlinkedModelSerializer
{% for model in models %}


class {{model.name}}(HyperlinkedModelSerializer):
    class Meta:
        model = models.{{model.name}}
        fields = "__all__"
{% endfor %}
"""

MODEL_TEMPLATE = """import uuid
from django.core import validators
from django.db import models
from jsonschema2dj.valdiators import JSONSchemaValidator
try:
    from django.contrib.postgres.fields import JSONField
except ImportError:
    pass
{% for model in models %}


class {{model.name}}(models.Model):

{% for name, (type, options) in model.field_str.items() %}
{% if type == "JSONField" %}
    {{name}} = JSONField(validators=[JSONSchemaValidator({{options["schema"]}})])
{% else %}
    {{name}} = models.{{type}}({% for k, v in options.items() %}{{k}}={{v}}, {% endfor %})
{% endif %}
{% endfor %}
{% for name, (type, model, options) in model.relations_str.items() %}
    {{name}} = models.{{type}}("{{model}}",{% for k, v in options.items() %}{{k}}={{v}},{% endfor %})
{% endfor %}
{% endfor %}
"""

URL_TEMPLATE = """from django.urls import path, include
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

ADMIN_TEMPLATE = """from django.contrib import admin
from . import models
{% for model in models %}


@admin.register(models.{{model.name}})
class {{model.name}}Admin(admin.ModelAdmin):
{% if model.enum_fields|length %}
    list_filter = (
{% for enum in model.enum_fields %}
        "{{enum}}",
{% endfor %}
    )
{% else %}
    pass
{% endif %}
{% endfor %}
"""

FILTER_TEMPLATE = """from django_filters import rest_framework as filters
from . import models
{% for model in models%}


class {{model.name}}(filters.FilterSet):
    class Meta:
        model = models.{{model.name}}
{% if model.filter_fields|length %}
        fields = {
{% for name, filter in model.filter_fields.items() %}
            "{{name}}": ["{{filter|join('", "') }}"],
{% endfor %}
        }
{% else %}
        fields = []
{% endif %}
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
