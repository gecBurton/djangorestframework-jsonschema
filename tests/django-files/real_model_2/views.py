from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from . import serializers, models, filters


class Book(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.Book
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Book
    ordering_fields = "__all__"
    search_fields = [
        "$title",
    ]


class Author(viewsets.ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.Author
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Author
    ordering_fields = "__all__"
    search_fields = [
        "$name",
    ]
