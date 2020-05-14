import uuid
from django.core import validators
from django.db import models
from jsonschema2dj.valdiators import JSONSchemaValidator
try:
    from django.contrib.postgres.fields import JSONField
except ImportError:
    pass
import pathlib

DEFINITIONS = str(pathlib.Path(__file__).parent.absolute() / "schema.json")


class Book(models.Model):

    title = models.CharField(null=True, max_length=255)
    genre = models.CharField(null=True, max_length=25, choices=[('celebrity_autobiographies', 'celebrity autobiographies'), ('military-history', 'military-history'), ('other', 'other')])
    min_reading_age = models.IntegerField(null=True, validators=[], choices=[(4, 4), (10, 10), (18, 18)])
    author = models.ForeignKey("Author", null=True, on_delete=models.CASCADE)
    other = JSONField(default = dict, null = True, validators=[JSONSchemaValidator({'$ref': '#/definitions/identifiers'}, DEFINITIONS)])


class Author(models.Model):

    name = models.CharField(null=True, max_length=255)
    date_of_birth = models.DateField(null=True)
