from django.contrib import admin
from . import models


@admin.register(models.Sample)
class SampleAdmin(admin.ModelAdmin):
    list_filter = (
        "hazaradous",
        "type",
    )


@admin.register(models.Patient)
class PatientAdmin(admin.ModelAdmin):
    list_filter = (
        "sex",
    )


@admin.register(models.Doctor)
class DoctorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Rack)
class RackAdmin(admin.ModelAdmin):
    list_filter = (
        "delivery_type",
    )
