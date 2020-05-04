from . import models
from rest_framework.serializers import ModelSerializer


class Author(ModelSerializer):
    class Meta:
        model = models.Author
        fields = "__all__"


class Book(ModelSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"
