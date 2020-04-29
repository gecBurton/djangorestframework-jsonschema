from django_filters import rest_framework as filters
from . import models


class A(filters.FilterSet):
    class Meta:
        model = models.A
        fields = []


class B(filters.FilterSet):
    class Meta:
        model = models.B
        fields = []


class C(filters.FilterSet):
    class Meta:
        model = models.C
        fields = []


class D(filters.FilterSet):
    class Meta:
        model = models.D
        fields = []


class E(filters.FilterSet):
    class Meta:
        model = models.E
        fields = []
