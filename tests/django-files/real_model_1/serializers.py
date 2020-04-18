from . import models
from rest_framework.serializers import HyperlinkedModelSerializer


class manifest(HyperlinkedModelSerializer):
    class Meta:
        model = models.manifest
        fields = "__all__"


class redcap(HyperlinkedModelSerializer):
    class Meta:
        model = models.redcap
        fields = "__all__"


class ResponsibleClinician(HyperlinkedModelSerializer):
    class Meta:
        model = models.ResponsibleClinician
        fields = "__all__"


class plate(HyperlinkedModelSerializer):
    class Meta:
        model = models.plate
        fields = "__all__"
