from . import models
from rest_framework.serializers import ModelSerializer


class person(ModelSerializer):
    class Meta:
        model = models.person
        fields = "__all__"
