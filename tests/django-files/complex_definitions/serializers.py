from . import models
from rest_framework.serializers import ModelSerializer


class field(ModelSerializer):
    class Meta:
        model = models.field
        fields = "__all__"


class model(ModelSerializer):
    class Meta:
        model = models.model
        fields = "__all__"
