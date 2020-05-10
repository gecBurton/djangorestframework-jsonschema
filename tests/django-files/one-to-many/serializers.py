from . import models
from rest_framework.serializers import ModelSerializer, ReadOnlyField


class PatientContact(ModelSerializer):
    class Meta:
        model = models.PatientContact
        fields = "__all__"


class Patient(ModelSerializer):
    class Meta:
        model = models.Patient
        fields = "__all__"
