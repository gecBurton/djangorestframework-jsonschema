from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from . import serializers, models, filters


class Sample(viewsets.ModelViewSet):
    queryset = models.Sample.objects.all()
    serializer_class = serializers.Sample
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Sample
    ordering_fields = "__all__"
    search_fields = [
        "$well",
    ]


class Patient(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.Patient
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Patient
    ordering_fields = "__all__"
    search_fields = [
        "$nhs_number",
        "$clinic",
    ]


class Doctor(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.Doctor
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Doctor
    ordering_fields = "__all__"
    search_fields = [
        "$name",
    ]


class Rack(viewsets.ModelViewSet):
    queryset = models.Rack.objects.all()
    serializer_class = serializers.Rack
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Rack
    ordering_fields = "__all__"
    search_fields = [
        "$id",
    ]
