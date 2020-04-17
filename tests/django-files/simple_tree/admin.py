
from django.contrib import admin
from . import models


@admin.register(models.F)
class FAdmin(admin.ModelAdmin):
    list_filter = ()

@admin.register(models.E)
class EAdmin(admin.ModelAdmin):
    list_filter = ()

@admin.register(models.D)
class DAdmin(admin.ModelAdmin):
    list_filter = ()

@admin.register(models.C)
class CAdmin(admin.ModelAdmin):
    list_filter = ()

@admin.register(models.B)
class BAdmin(admin.ModelAdmin):
    list_filter = ()

@admin.register(models.A)
class AAdmin(admin.ModelAdmin):
    list_filter = ()
