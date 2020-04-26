from django_filters import rest_framework as filters
from . import models


class Manifest(filters.FilterSet):
    class Meta:
        model = models.Manifest
        fields = {
            "sample_id": ["exact", "gte", "lte"],
            "volume_ul": ["exact", "gte", "lte"],
            "concentration_ng_ul": ["exact", "gte", "lte"],
            "od_260_280": ["exact", "gte", "lte"],
            "cancer_sample_y_n": ["exact", "in"],
            "sample_type": ["exact", "in"],
        }


class Redcap(filters.FilterSet):
    class Meta:
        model = models.Redcap
        fields = {
            "sex": ["exact", "in"],
            "date_of_birth": ["exact", "gte", "lte"],
            "date_of_identifying_eligibility_for_the_study": ["exact", "gte", "lte"],
        }


class ResponsibleClinician(filters.FilterSet):
    class Meta:
        model = models.ResponsibleClinician
        fields = []


class Plate(filters.FilterSet):
    class Meta:
        model = models.Plate
        fields = {
            "priority": ["exact", "in"],
        }
