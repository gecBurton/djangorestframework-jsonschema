from django_filters import rest_framework as filters
from . import models


class Patient(filters.FilterSet):
    class Meta:
        model = models.Patient
        fields = []
