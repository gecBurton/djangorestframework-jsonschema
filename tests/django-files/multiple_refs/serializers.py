from . import models
from rest_framework.serializers import ModelSerializer, ReadOnlyField


class Patient(ModelSerializer):
    class Meta:
        model = models.Patient
        fields = "__all__"
