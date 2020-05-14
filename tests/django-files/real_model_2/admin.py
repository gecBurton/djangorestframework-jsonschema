from django.contrib import admin
from . import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = (
        "genre",
        "min_reading_age",
    )


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
