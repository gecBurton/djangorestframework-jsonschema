from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from . import serializers, models, filters


class PatientContact(viewsets.ModelViewSet):
    queryset = models.PatientContact.objects.all()
    serializer_class = serializers.PatientContact
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.PatientContact
    ordering_fields = "__all__"


class Patient(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.Patient
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Patient
    ordering_fields = "__all__"
