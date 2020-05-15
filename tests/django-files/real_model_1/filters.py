from django_filters import rest_framework as filters
from . import models


class Sample(filters.FilterSet):
    class Meta:
        model = models.Sample
        fields = {
            "sample_id": ["exact", "gte", "lte"],
            "percentage": ["exact", "gte", "lte"],
            "hazaradous": ["exact", "in"],
            "type": ["exact", "in"],
        }


class Patient(filters.FilterSet):
    class Meta:
        model = models.Patient
        fields = {
            "sex": ["exact", "in"],
            "DOB": ["exact", "gte", "lte"],
        }


class Doctor(filters.FilterSet):
    class Meta:
        model = models.Doctor
        fields = []


class Rack(filters.FilterSet):
    class Meta:
        model = models.Rack
        fields = {
            "delivery_type": ["exact", "in"],
        }
