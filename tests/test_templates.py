from json import load
import pytest

from jsonschema2dj.models import Model, build_dependency_order
from jsonschema2dj.templates import (
    build_models,
    build_serializers,
    build_views,
    build_urls,
    build_admin,
)

with open("tests/schemas/basic_model.json") as f:
    basic_model = load(f)

with open("tests/schemas/simple_tree.json") as f:
    simple_tree = load(f)


result_1 = """
import uuid
from django.core import validators
from django.db import models


class person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(null=False, max_length=255)
    age = models.IntegerField(null=False, validators=[validators.MinValueValidator(0)])
    sex = models.CharField(null=True, max_length=6, choices=[('male', 'male'), ('female', 'female')])


"""

serializer_1 = """
from . import models
from rest_framework.serializers import ModelSerializer



class person(ModelSerializer):

    class Meta:
        model = models.person
        fields = '__all__'

"""

result_2 = """
import uuid
from django.core import validators
from django.db import models


class F(models.Model):



class D(models.Model):



class C(models.Model):

    d = models.ForeignKey(D, null=True, on_delete=models.CASCADE)


class E(models.Model):

    f = models.ForeignKey(F, null=True, on_delete=models.CASCADE)


class B(models.Model):

    c = models.ForeignKey(C, null=True, on_delete=models.CASCADE)
    e = models.ForeignKey(E, null=True, on_delete=models.CASCADE)


class A(models.Model):

    b = models.ForeignKey(B, null=True, on_delete=models.CASCADE)

"""

serializer_2 = """
from . import models
from rest_framework.serializers import ModelSerializer



class F(ModelSerializer):

    class Meta:
        model = models.F
        fields = '__all__'


class D(ModelSerializer):

    class Meta:
        model = models.D
        fields = '__all__'


class C(ModelSerializer):

    class Meta:
        model = models.C
        fields = '__all__'


class E(ModelSerializer):

    class Meta:
        model = models.E
        fields = '__all__'


class B(ModelSerializer):

    class Meta:
        model = models.B
        fields = '__all__'


class A(ModelSerializer):

    class Meta:
        model = models.A
        fields = '__all__'

"""

admin_1 = """
from django.contrib import admin
from . import models


@admin.register(models.person)
class personAdmin(admin.ModelAdmin):
    list_filter = (
        "sex",
    )
"""

admin_2 = """
from django.contrib import admin
from . import models


@admin.register(models.F)
class FAdmin(admin.ModelAdmin):
    list_filter = (
    )

@admin.register(models.D)
class DAdmin(admin.ModelAdmin):
    list_filter = (
    )

@admin.register(models.C)
class CAdmin(admin.ModelAdmin):
    list_filter = (
    )

@admin.register(models.E)
class EAdmin(admin.ModelAdmin):
    list_filter = (
    )

@admin.register(models.B)
class BAdmin(admin.ModelAdmin):
    list_filter = (
    )

@admin.register(models.A)
class AAdmin(admin.ModelAdmin):
    list_filter = (
    )
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

router.register("D", views.D)

router.register("C", views.C)

router.register("E", views.E)

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


class D(viewsets.ModelViewSet):
    queryset = models.D.objects.all()
    serializer_class = serializers.D
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.D
    ordering_fields = "__all__"


class C(viewsets.ModelViewSet):
    queryset = models.C.objects.all()
    serializer_class = serializers.C
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.C
    ordering_fields = "__all__"


class E(viewsets.ModelViewSet):
    queryset = models.E.objects.all()
    serializer_class = serializers.E
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.E
    ordering_fields = "__all__"


class B(viewsets.ModelViewSet):
    queryset = models.B.objects.all()
    serializer_class = serializers.B
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.B
    ordering_fields = "__all__"


class A(viewsets.ModelViewSet):
    queryset = models.A.objects.all()
    serializer_class = serializers.A
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.A
    ordering_fields = "__all__"

"""

@pytest.mark.parametrize(
    "schema,model,serializer,admin,url,view",
    [
        (basic_model, result_1, serializer_1, admin_1, urls_1, view_1),
        (simple_tree, result_2, serializer_2, admin_2, urls_2, view_2),
    ],
)
def test_build_models(schema, model, serializer, admin, url, view):
    models = [
        Model(model_name, schema["definitions"][model_name])
        for model_name in build_dependency_order(schema)
    ]

    assert build_models(models) == model
    assert build_serializers(models) == serializer
    assert build_admin(models) == admin
    assert build_urls(models) == url
    assert build_views(models) == view


