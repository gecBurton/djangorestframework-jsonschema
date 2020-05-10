from django_filters import rest_framework as filters
from . import models


class PatientContact(filters.FilterSet):
    class Meta:
        model = models.PatientContact
        fields = {
            "gender": ["exact", "in"],
        }


class Patient(filters.FilterSet):
    class Meta:
        model = models.Patient
        fields = {
            "birthDate": ["exact", "gte", "lte"],
        }
