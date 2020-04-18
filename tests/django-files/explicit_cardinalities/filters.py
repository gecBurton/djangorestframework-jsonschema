from django_filters import rest_framework as filters
from . import models


class A(filters.FilterSet):
    class Meta:
        model = models.A


class B(filters.FilterSet):
    class Meta:
        model = models.B


class C(filters.FilterSet):
    class Meta:
        model = models.C


class D(filters.FilterSet):
    class Meta:
        model = models.D


class E(filters.FilterSet):
    class Meta:
        model = models.E
