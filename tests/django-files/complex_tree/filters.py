from django_filters import rest_framework as filters
from . import models


class Hospital(filters.FilterSet):
    class Meta:
        model = models.Hospital
        fields = {
            "type": ["exact", "in"],
        }


class Doctor(filters.FilterSet):
    class Meta:
        model = models.Doctor


class Patient(filters.FilterSet):
    class Meta:
        model = models.Patient
