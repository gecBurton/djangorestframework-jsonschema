
from django.contrib import admin
from . import models


@admin.register(models.person)
class personAdmin(admin.ModelAdmin):
    list_filter = ("sex", )
