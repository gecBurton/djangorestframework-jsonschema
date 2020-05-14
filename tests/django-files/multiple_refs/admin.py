from django.contrib import admin
from . import models


@admin.register(models.Patient)
class PatientAdmin(admin.ModelAdmin):
    pass
