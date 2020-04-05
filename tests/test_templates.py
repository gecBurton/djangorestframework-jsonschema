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


class personModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    name = models.CharField(null=False, max_length=255)

    age = models.IntegerField(null=False, validators=[validators.MinValueValidator(0)])

    sex = models.CharField(null=True, max_length=6, choices=[('male', 'male'), ('female', 'female')])




"""

serializer_1 = """
from . import models
from rest_framework.serializers import ModelSerializer



class personSerializer(ModelSerializer):

    class Meta:
        model = models.personModel
        fields = '__all__'

"""

result_2 = """
import uuid
from django.core import validators
from django.db import models


class FModel(models.Model):





class DModel(models.Model):





class CModel(models.Model):




    d = models.ForeignKey(DModel, null=True, on_delete=models.CASCADE)




class EModel(models.Model):




    f = models.ForeignKey(FModel, null=True, on_delete=models.CASCADE)




class BModel(models.Model):




    c = models.ForeignKey(CModel, null=True, on_delete=models.CASCADE)



    e = models.ForeignKey(EModel, null=True, on_delete=models.CASCADE)




class AModel(models.Model):




    b = models.ForeignKey(BModel, null=True, on_delete=models.CASCADE)



"""

serializer_2 = """
from . import models
from rest_framework.serializers import ModelSerializer



class FSerializer(ModelSerializer):

    class Meta:
        model = models.FModel
        fields = '__all__'


class DSerializer(ModelSerializer):

    class Meta:
        model = models.DModel
        fields = '__all__'


class CSerializer(ModelSerializer):

    class Meta:
        model = models.CModel
        fields = '__all__'


class ESerializer(ModelSerializer):

    class Meta:
        model = models.EModel
        fields = '__all__'


class BSerializer(ModelSerializer):

    class Meta:
        model = models.BModel
        fields = '__all__'


class ASerializer(ModelSerializer):

    class Meta:
        model = models.AModel
        fields = '__all__'

"""

admin_1 = """
from django.contrib import admin
from . import models


@admin.register(models.personModel)
class personAdmin(admin.ModelAdmin):
    list_filter = (

        "sex",

    )
"""

admin_2 = """
from django.contrib import admin
from . import models


@admin.register(models.FModel)
class FAdmin(admin.ModelAdmin):
    list_filter = (

    )

@admin.register(models.DModel)
class DAdmin(admin.ModelAdmin):
    list_filter = (

    )

@admin.register(models.CModel)
class CAdmin(admin.ModelAdmin):
    list_filter = (

    )

@admin.register(models.EModel)
class EAdmin(admin.ModelAdmin):
    list_filter = (

    )

@admin.register(models.BModel)
class BAdmin(admin.ModelAdmin):
    list_filter = (

    )

@admin.register(models.AModel)
class AAdmin(admin.ModelAdmin):
    list_filter = (

    )
"""

view_1 = """
from rest_framework import viewsets
from . import serializers, models


class personViewSet(viewsets.ModelViewSet):
    queryset = models.personModel.objects.all()
    serializer_class = serializers.personSerializer

"""

urls_1 = """
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()


router.register("person", views.personViewSet)


urlpatterns = [
    path("", include(router.urls)),
]"""

urls_2 = """
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()


router.register("F", views.FViewSet)

router.register("D", views.DViewSet)

router.register("C", views.CViewSet)

router.register("E", views.EViewSet)

router.register("B", views.BViewSet)

router.register("A", views.AViewSet)


urlpatterns = [
    path("", include(router.urls)),
]"""

view_2 = """
from rest_framework import viewsets
from . import serializers, models


class FViewSet(viewsets.ModelViewSet):
    queryset = models.FModel.objects.all()
    serializer_class = serializers.FSerializer


class DViewSet(viewsets.ModelViewSet):
    queryset = models.DModel.objects.all()
    serializer_class = serializers.DSerializer


class CViewSet(viewsets.ModelViewSet):
    queryset = models.CModel.objects.all()
    serializer_class = serializers.CSerializer


class EViewSet(viewsets.ModelViewSet):
    queryset = models.EModel.objects.all()
    serializer_class = serializers.ESerializer


class BViewSet(viewsets.ModelViewSet):
    queryset = models.BModel.objects.all()
    serializer_class = serializers.BSerializer


class AViewSet(viewsets.ModelViewSet):
    queryset = models.AModel.objects.all()
    serializer_class = serializers.ASerializer

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


