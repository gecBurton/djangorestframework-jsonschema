from . import models
from rest_framework.serializers import ModelSerializer, ReadOnlyField


class Book(ModelSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"


class Author(ModelSerializer):
    class Meta:
        model = models.Author
        fields = "__all__"
