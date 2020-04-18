from . import models
from rest_framework.serializers import HyperlinkedModelSerializer


class A(HyperlinkedModelSerializer):
    class Meta:
        model = models.A
        fields = "__all__"


class B(HyperlinkedModelSerializer):
    class Meta:
        model = models.B
        fields = "__all__"


class C(HyperlinkedModelSerializer):
    class Meta:
        model = models.C
        fields = "__all__"


class D(HyperlinkedModelSerializer):
    class Meta:
        model = models.D
        fields = "__all__"


class E(HyperlinkedModelSerializer):
    class Meta:
        model = models.E
        fields = "__all__"
