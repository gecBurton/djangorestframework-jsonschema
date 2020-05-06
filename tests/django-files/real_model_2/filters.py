from django_filters import rest_framework as filters
from . import models


class Book(filters.FilterSet):
    class Meta:
        model = models.Book
        fields = {
            "genre": ["exact", "in"],
        }


class Author(filters.FilterSet):
    class Meta:
        model = models.Author
        fields = {
            "date_of_birth": ["exact", "gte", "lte"],
        }
