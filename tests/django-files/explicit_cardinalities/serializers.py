from . import models
from rest_framework.serializers import ModelSerializer


class A(ModelSerializer):
    class Meta:
        model = models.A
        fields = "__all__"


class B(ModelSerializer):
    class Meta:
        model = models.B
        fields = "__all__"


class C(ModelSerializer):
    class Meta:
        model = models.C
        fields = "__all__"


class D(ModelSerializer):
    class Meta:
        model = models.D
        fields = "__all__"


class E(ModelSerializer):
    class Meta:
        model = models.E
        fields = "__all__"
