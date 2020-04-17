
from django_filters import rest_framework as filters
from . import models

class F(filters.FilterSet):
    class Meta:
        model = models.F
        fields = {
            }


class E(filters.FilterSet):
    class Meta:
        model = models.E
        fields = {
            }


class D(filters.FilterSet):
    class Meta:
        model = models.D
        fields = {
            }


class C(filters.FilterSet):
    class Meta:
        model = models.C
        fields = {
            }


class B(filters.FilterSet):
    class Meta:
        model = models.B
        fields = {
            }


class A(filters.FilterSet):
    class Meta:
        model = models.A
        fields = {
            }


