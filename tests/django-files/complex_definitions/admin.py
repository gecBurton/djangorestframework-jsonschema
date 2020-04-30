from django.contrib import admin
from . import models


@admin.register(models.field)
class fieldAdmin(admin.ModelAdmin):
    pass


@admin.register(models.model)
class modelAdmin(admin.ModelAdmin):
    pass
