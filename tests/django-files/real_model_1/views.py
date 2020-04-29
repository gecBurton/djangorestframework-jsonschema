from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from . import serializers, models, filters


class Manifest(viewsets.ModelViewSet):
    queryset = models.Manifest.objects.all()
    serializer_class = serializers.Manifest
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Manifest
    ordering_fields = "__all__"
    search_fields = [
        "$well",
    ]


class Redcap(viewsets.ModelViewSet):
    queryset = models.Redcap.objects.all()
    serializer_class = serializers.Redcap
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Redcap
    ordering_fields = "__all__"
    search_fields = [
        "$GenOMICC",
        "$nhs_number",
        "$hospital_trust",
    ]


class ResponsibleClinician(viewsets.ModelViewSet):
    queryset = models.ResponsibleClinician.objects.all()
    serializer_class = serializers.ResponsibleClinician
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ResponsibleClinician
    ordering_fields = "__all__"
    search_fields = [
        "$name",
    ]


class Plate(viewsets.ModelViewSet):
    queryset = models.Plate.objects.all()
    serializer_class = serializers.Plate
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Plate
    ordering_fields = "__all__"
    search_fields = [
        "$barcode",
    ]
