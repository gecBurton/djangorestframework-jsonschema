from json import load
import pytest

from jsonschema2dj.models import Model, build_dependency_order
from jsonschema2dj.templates import build_models, build_serializers, build_views, build_urls

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
from drf_writable_nested.serializers import WritableNestedModelSerialize



class personSerializer(WritableNestedModelSerializer):


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



    d = models.ForeignKey(CModel, null=True, on_delete=models.CASCADE)



class EModel(models.Model):



    f = models.ForeignKey(EModel, null=True, on_delete=models.CASCADE)



class BModel(models.Model):



    c = models.ForeignKey(BModel, null=True, on_delete=models.CASCADE)

    e = models.ForeignKey(BModel, null=True, on_delete=models.CASCADE)



class AModel(models.Model):



    b = models.ForeignKey(AModel, null=True, on_delete=models.CASCADE)


"""

serializer_2 = """
from . import models
from drf_writable_nested.serializers import WritableNestedModelSerialize



class FSerializer(WritableNestedModelSerializer):


    class Meta:
        model = models.FModel
        fields = '__all__'


class DSerializer(WritableNestedModelSerializer):


    class Meta:
        model = models.DModel
        fields = '__all__'


class CSerializer(WritableNestedModelSerializer):


    class Meta:
        model = models.CModel
        fields = '__all__'


class ESerializer(WritableNestedModelSerializer):


    class Meta:
        model = models.EModel
        fields = '__all__'


class BSerializer(WritableNestedModelSerializer):


    class Meta:
        model = models.BModel
        fields = '__all__'


class ASerializer(WritableNestedModelSerializer):


    class Meta:
        model = models.AModel
        fields = '__all__'

"""

@pytest.mark.parametrize("schema,result,serializer", [(basic_model, result_1, serializer_1), (simple_tree, result_2, serializer_2)])
def test_build_models(schema, result, serializer):
    model = [
            Model(model_name, schema["definitions"][model_name])
            for model_name in build_dependency_order(schema)
        ]

    assert build_models(model) == result
    assert build_serializers(model) == serializer

view = """
from rest_framework import viewsets
from . import serializers, models


class personViewSet(viewsets.ModelViewSet):
    queryset = models.;personModel.objects.all()
    serializer_class = serializers.personSerializer

"""

urls = """
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()


router.register(person, person)


urlpatterns = [
    path("", include(router.urls)),
]"""

def test_views_urls():
    views = [(a, b["$ref"].split("/")[-1]) for a, b in basic_model["properties"].items()]
    assert build_views(views) == view
    assert build_urls(views) == urls
