
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from . import serializers, models, filters


class manifest(viewsets.ModelViewSet):
    queryset = models.manifest.objects.all()
    serializer_class = serializers.manifest
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.manifest
    ordering_fields = "__all__"
    search_fields = ["$well", ]



class redcap(viewsets.ModelViewSet):
    queryset = models.redcap.objects.all()
    serializer_class = serializers.redcap
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.redcap
    ordering_fields = "__all__"
    search_fields = ["$GenOMICC", "$nhs_number", "$hospital_trust", ]



class ResponsibleClinician(viewsets.ModelViewSet):
    queryset = models.ResponsibleClinician.objects.all()
    serializer_class = serializers.ResponsibleClinician
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ResponsibleClinician
    ordering_fields = "__all__"
    search_fields = ["$name", ]



class plate(viewsets.ModelViewSet):
    queryset = models.plate.objects.all()
    serializer_class = serializers.plate
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.plate
    ordering_fields = "__all__"
    search_fields = ["$barcode", ]


