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


class person(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(validators=[validators.MinValueValidator(0)])
    sex = models.CharField(null=True, max_length=6, choices=[('male', 'male'), ('female', 'female')])
