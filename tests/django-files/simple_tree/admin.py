from django.contrib import admin
from . import models


@admin.register(models.F)
class FAdmin(admin.ModelAdmin):
    pass


@admin.register(models.E)
class EAdmin(admin.ModelAdmin):
    pass


@admin.register(models.D)
class DAdmin(admin.ModelAdmin):
    pass


@admin.register(models.C)
class CAdmin(admin.ModelAdmin):
    pass


@admin.register(models.B)
class BAdmin(admin.ModelAdmin):
    pass


@admin.register(models.A)
class AAdmin(admin.ModelAdmin):
    pass
