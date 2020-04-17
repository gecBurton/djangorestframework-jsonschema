
from django.contrib import admin
from . import models


@admin.register(models.Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_filter = ("type", )

@admin.register(models.Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_filter = ()

@admin.register(models.Patient)
class PatientAdmin(admin.ModelAdmin):
    list_filter = ()
