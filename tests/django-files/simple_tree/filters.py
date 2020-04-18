from django_filters import rest_framework as filters
from . import models


class F(filters.FilterSet):
    class Meta:
        model = models.F


class E(filters.FilterSet):
    class Meta:
        model = models.E


class D(filters.FilterSet):
    class Meta:
        model = models.D


class C(filters.FilterSet):
    class Meta:
        model = models.C


class B(filters.FilterSet):
    class Meta:
        model = models.B


class A(filters.FilterSet):
    class Meta:
        model = models.A
