from . import models
from rest_framework.serializers import HyperlinkedModelSerializer


class Hospital(HyperlinkedModelSerializer):
    class Meta:
        model = models.Hospital
        fields = "__all__"


class Doctor(HyperlinkedModelSerializer):
    class Meta:
        model = models.Doctor
        fields = "__all__"


class Patient(HyperlinkedModelSerializer):
    class Meta:
        model = models.Patient
        fields = "__all__"
