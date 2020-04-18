from . import models
from rest_framework.serializers import HyperlinkedModelSerializer


class person(HyperlinkedModelSerializer):
    class Meta:
        model = models.person
        fields = "__all__"
