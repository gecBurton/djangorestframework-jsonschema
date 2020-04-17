
from django_filters import rest_framework as filters
from . import models

class person(filters.FilterSet):
    class Meta:
        model = models.person
        fields = {
            "age": ["exact", "gte", "lte"],
            "sex": ["exact", "in"],
            }


