import uuid
from django.core import validators
from django.db import models
from jsonschema2dj.valdiators import JSONSchemaValidator
try:
    from django.contrib.postgres.fields import JSONField
except ImportError:
    pass


class Book(models.Model):

    title = models.CharField(max_length=255)
    pages = models.IntegerField(validators=[validators.MinValueValidator(0)])
    genre = models.CharField(max_length=25, choices=[('celebrity_autobiographies', 'celebrity autobiographies'), ('military-history', 'military-history'), ('other', 'other')])
    author = models.ForeignKey("Author", on_delete=models.CASCADE)


class Author(models.Model):

    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
