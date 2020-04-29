from . import models
from rest_framework.serializers import ModelSerializer


class Hospital(ModelSerializer):
    class Meta:
        model = models.Hospital
        fields = "__all__"


class Doctor(ModelSerializer):
    class Meta:
        model = models.Doctor
        fields = "__all__"


class Patient(ModelSerializer):
    class Meta:
        model = models.Patient
        fields = "__all__"
