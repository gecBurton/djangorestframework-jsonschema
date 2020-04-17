
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from . import serializers, models, filters


class person(viewsets.ModelViewSet):
    queryset = models.person.objects.all()
    serializer_class = serializers.person
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.person
    ordering_fields = "__all__"
    search_fields = ["$name", ]


