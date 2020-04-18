from json import load
import pytest

from jsonschema2dj.models import Model, build_relationships
from jsonschema2dj.templates import (
    build_models,
    build_serializers,
    build_views,
    build_urls,
    build_admin,
    build_filters,
)

with open("tests/json-schemas/basic_model.json") as f:
    basic_model = load(f)

with open("tests/json-schemas/simple_tree.json") as f:
    simple_tree = load(f)


result_1 = """
import uuid
from django.core import validators
from django.db import models
try:
    from extra_fields import JSONSchemaField
except ImportError:
    pass


class person(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, )
    name = models.CharField(null=False, primary_key=False, max_length=255, )
    age = models.IntegerField(null=False, validators=[validators.MinValueValidator(0)], primary_key=False, )
    sex = models.CharField(null=True, primary_key=False, max_length=6, choices=[('male', 'male'), ('female', 'female')], )


"""

serializer_1 = """
from . import models
from rest_framework.serializers import HyperlinkedModelSerializer



class person(HyperlinkedModelSerializer):

    class Meta:
        model = models.person
        fields = '__all__'

"""

result_2 = """
import uuid
from django.core import validators
from django.db import models
try:
    from extra_fields import JSONSchemaField
except ImportError:
    pass


class F(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=False, )



class E(models.Model):

    f = models.ForeignKey("F", null=True, on_delete=models.CASCADE, )


class D(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=False, )



class C(models.Model):

    d = models.ForeignKey("D", null=True, on_delete=models.CASCADE, )


class B(models.Model):

    c = models.ForeignKey("C", null=True, on_delete=models.CASCADE, )
    e = models.ForeignKey("E", null=True, on_delete=models.CASCADE, )


class A(models.Model):

    b = models.ForeignKey("B", null=True, on_delete=models.CASCADE, )

"""

serializer_2 = """
from . import models
from rest_framework.serializers import HyperlinkedModelSerializer



class F(HyperlinkedModelSerializer):

    class Meta:
        model = models.F
        fields = '__all__'


class E(HyperlinkedModelSerializer):

    class Meta:
        model = models.E
        fields = '__all__'


class D(HyperlinkedModelSerializer):

    class Meta:
        model = models.D
        fields = '__all__'


class C(HyperlinkedModelSerializer):

    class Meta:
        model = models.C
        fields = '__all__'


class B(HyperlinkedModelSerializer):

    class Meta:
        model = models.B
        fields = '__all__'


class A(HyperlinkedModelSerializer):

    class Meta:
        model = models.A
        fields = '__all__'

"""

admin_1 = """
from django.contrib import admin
from . import models


@admin.register(models.person)
class personAdmin(admin.ModelAdmin):
    list_filter = ("sex", )
"""

admin_2 = """
from django.contrib import admin
from . import models


@admin.register(models.F)
class FAdmin(admin.ModelAdmin):
    list_filter = ()

@admin.register(models.E)
class EAdmin(admin.ModelAdmin):
    list_filter = ()

@admin.register(models.D)
class DAdmin(admin.ModelAdmin):
    list_filter = ()

@admin.register(models.C)
class CAdmin(admin.ModelAdmin):
    list_filter = ()

@admin.register(models.B)
class BAdmin(admin.ModelAdmin):
    list_filter = ()

@admin.register(models.A)
class AAdmin(admin.ModelAdmin):
    list_filter = ()
"""

view_1 = """
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from . import serializers, models, filters


class person(viewsets.ModelViewSet):
    queryset = models.person.objects.all()
    serializer_class = serializers.person
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.person
    ordering_fields = "__all__"
    search_fields = ["$name", ]


"""

urls_1 = """
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register("person", views.person)

urlpatterns = [
    path("", include(router.urls)),
]"""

urls_2 = """
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register("F", views.F)
router.register("E", views.E)
router.register("D", views.D)
router.register("C", views.C)
router.register("B", views.B)
router.register("A", views.A)

urlpatterns = [
    path("", include(router.urls)),
]"""

view_2 = """
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from . import serializers, models, filters


class F(viewsets.ModelViewSet):
    queryset = models.F.objects.all()
    serializer_class = serializers.F
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.F
    ordering_fields = "__all__"
    search_fields = []



class E(viewsets.ModelViewSet):
    queryset = models.E.objects.all()
    serializer_class = serializers.E
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.E
    ordering_fields = "__all__"
    search_fields = []



class D(viewsets.ModelViewSet):
    queryset = models.D.objects.all()
    serializer_class = serializers.D
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.D
    ordering_fields = "__all__"
    search_fields = []



class C(viewsets.ModelViewSet):
    queryset = models.C.objects.all()
    serializer_class = serializers.C
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.C
    ordering_fields = "__all__"
    search_fields = []



class B(viewsets.ModelViewSet):
    queryset = models.B.objects.all()
    serializer_class = serializers.B
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.B
    ordering_fields = "__all__"
    search_fields = []



class A(viewsets.ModelViewSet):
    queryset = models.A.objects.all()
    serializer_class = serializers.A
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.A
    ordering_fields = "__all__"
    search_fields = []


"""

filter_1 = """
from django_filters import rest_framework as filters
from . import models

class person(filters.FilterSet):
    class Meta:
        model = models.person
        fields = {
            "age": ["exact", "gte", "lte"],
            "sex": ["exact", "in"],
            }


"""

filter_2 = """
from django_filters import rest_framework as filters
from . import models

class F(filters.FilterSet):
    class Meta:
        model = models.F
        fields = {
            }


class E(filters.FilterSet):
    class Meta:
        model = models.E
        fields = {
            }


class D(filters.FilterSet):
    class Meta:
        model = models.D
        fields = {
            }


class C(filters.FilterSet):
    class Meta:
        model = models.C
        fields = {
            }


class B(filters.FilterSet):
    class Meta:
        model = models.B
        fields = {
            }


class A(filters.FilterSet):
    class Meta:
        model = models.A
        fields = {
            }


"""


@pytest.mark.parametrize(
    "schema,model,serializer,admin,url,view,filter",
    [
        #     (basic_model, result_1, serializer_1, admin_1, urls_1, view_1, filter_1),
        (simple_tree, result_2, serializer_2, admin_2, urls_2, view_2, filter_2),
    ],
)
def test_build_models(schema, model, serializer, admin, url, view, filter):
    models = [
        Model(model_name, schema["definitions"][model_name], **kwargs)
        for model_name, kwargs in build_relationships(schema).items()
    ]

    assert build_models(models) == model
    assert build_serializers(models) == serializer
    assert build_admin(models) == admin
    assert build_urls(models) == url
    assert build_views(models) == view
    assert build_filters(models) == filter
