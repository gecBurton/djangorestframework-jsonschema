from . import models
from rest_framework.serializers import ModelSerializer, ReadOnlyField


class person(ModelSerializer):
    class Meta:
        model = models.person
        fields = "__all__"
