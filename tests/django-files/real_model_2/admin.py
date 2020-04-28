from django.contrib import admin
from . import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = (
        "genre",
    )


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
