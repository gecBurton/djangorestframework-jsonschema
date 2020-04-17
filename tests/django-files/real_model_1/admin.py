
from django.contrib import admin
from . import models


@admin.register(models.manifest)
class manifestAdmin(admin.ModelAdmin):
    list_filter = ("cancer_sample_y_n", "sample_type", )

@admin.register(models.redcap)
class redcapAdmin(admin.ModelAdmin):
    list_filter = ("sex", )

@admin.register(models.ResponsibleClinician)
class ResponsibleClinicianAdmin(admin.ModelAdmin):
    list_filter = ()

@admin.register(models.plate)
class plateAdmin(admin.ModelAdmin):
    list_filter = ("priority", )
