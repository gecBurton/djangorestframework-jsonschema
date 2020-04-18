import uuid
from django.core import validators
from django.db import models

try:
    from extra_fields import JSONSchemaField
except ImportError:
    pass


class person(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True,)
    name = models.CharField(null=False, primary_key=False, max_length=255,)
    age = models.IntegerField(
        null=False, validators=[validators.MinValueValidator(0)], primary_key=False,
    )
    sex = models.CharField(
        null=True,
        primary_key=False,
        max_length=6,
        choices=[("male", "male"), ("female", "female")],
    )
