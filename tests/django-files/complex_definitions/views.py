from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from . import serializers, models, filters


class model(viewsets.ModelViewSet):
    queryset = models.model.objects.all()
    serializer_class = serializers.model
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.model
    ordering_fields = "__all__"
