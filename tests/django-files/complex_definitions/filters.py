from django_filters import rest_framework as filters
from . import models


class model(filters.FilterSet):
    class Meta:
        model = models.model
        fields = {
            "field_2": ["exact", "gte", "lte"],
        }
