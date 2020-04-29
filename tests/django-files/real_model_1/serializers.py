from . import models
from rest_framework.serializers import ModelSerializer


class Manifest(ModelSerializer):
    class Meta:
        model = models.Manifest
        fields = "__all__"


class Redcap(ModelSerializer):
    class Meta:
        model = models.Redcap
        fields = "__all__"


class ResponsibleClinician(ModelSerializer):
    class Meta:
        model = models.ResponsibleClinician
        fields = "__all__"


class Plate(ModelSerializer):
    class Meta:
        model = models.Plate
        fields = "__all__"
