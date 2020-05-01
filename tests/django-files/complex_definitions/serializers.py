from . import models
from rest_framework.serializers import ModelSerializer


class model(ModelSerializer):
    class Meta:
        model = models.model
        fields = "__all__"
