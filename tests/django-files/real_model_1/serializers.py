from . import models
from rest_framework.serializers import ModelSerializer, ReadOnlyField


class Sample(ModelSerializer):
    class Meta:
        model = models.Sample
        fields = "__all__"


class Patient(ModelSerializer):
    class Meta:
        model = models.Patient
        fields = "__all__"


class Doctor(ModelSerializer):
    class Meta:
        model = models.Doctor
        fields = "__all__"


class Rack(ModelSerializer):
    type = ReadOnlyField(default='SAMPLE_RACK')
    class Meta:
        model = models.Rack
        fields = "__all__"
