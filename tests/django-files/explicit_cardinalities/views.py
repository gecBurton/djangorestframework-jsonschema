from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from . import serializers, models, filters


class A(viewsets.ModelViewSet):
    queryset = models.A.objects.all()
    serializer_class = serializers.A
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.A
    ordering_fields = "__all__"


class B(viewsets.ModelViewSet):
    queryset = models.B.objects.all()
    serializer_class = serializers.B
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.B
    ordering_fields = "__all__"


class C(viewsets.ModelViewSet):
    queryset = models.C.objects.all()
    serializer_class = serializers.C
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.C
    ordering_fields = "__all__"


class D(viewsets.ModelViewSet):
    queryset = models.D.objects.all()
    serializer_class = serializers.D
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.D
    ordering_fields = "__all__"


class E(viewsets.ModelViewSet):
    queryset = models.E.objects.all()
    serializer_class = serializers.E
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.E
    ordering_fields = "__all__"
