from django.contrib import admin
from . import models


@admin.register(models.PatientContact)
class PatientContactAdmin(admin.ModelAdmin):
    list_filter = (
        "gender",
    )


@admin.register(models.Patient)
class PatientAdmin(admin.ModelAdmin):
    pass
