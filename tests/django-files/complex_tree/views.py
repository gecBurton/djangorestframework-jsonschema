
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from . import serializers, models, filters


class Hospital(viewsets.ModelViewSet):
    queryset = models.Hospital.objects.all()
    serializer_class = serializers.Hospital
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Hospital
    ordering_fields = "__all__"
    search_fields = ["$postcode", ]



class Doctor(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.Doctor
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Doctor
    ordering_fields = "__all__"
    search_fields = ["$name", ]



class Patient(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.Patient
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Patient
    ordering_fields = "__all__"
    search_fields = ["$nhs_number", ]


