from django.contrib import admin
from . import models


@admin.register(models.Manifest)
class ManifestAdmin(admin.ModelAdmin):
    list_filter = (
        "cancer_sample_y_n",
        "sample_type",
    )


@admin.register(models.Redcap)
class RedcapAdmin(admin.ModelAdmin):
    list_filter = (
        "sex",
    )


@admin.register(models.ResponsibleClinician)
class ResponsibleClinicianAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Plate)
class PlateAdmin(admin.ModelAdmin):
    list_filter = (
        "priority",
    )
