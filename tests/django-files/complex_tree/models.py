import uuid
from django.core import validators
from django.db import models

try:
    from extra_fields import JSONSchemaField
except ImportError:
    pass


class Hospital(models.Model):
    postcode = models.CharField(
        null=False,
        primary_key=False,
        max_length=255,
        validators=[("RegexValidator", 'r"^[a-z]{1,2}\\d[a-z\\d]?\\s*\\d[a-z]{2}$"')],
    )
    type = models.CharField(
        null=False,
        primary_key=False,
        max_length=7,
        choices=[("general", "general"), ("local", "local"), ("clinic", "clinic")],
    )


class Doctor(models.Model):
    name = models.CharField(null=False, primary_key=False, max_length=255,)

    hospital = models.ForeignKey("Hospital", null=True, on_delete=models.CASCADE,)
    patient = models.ManyToManyField("Patient", null=True, on_delete=models.CASCADE,)


class Patient(models.Model):
    nhs_number = models.CharField(
        null=False,
        primary_key=False,
        max_length=255,
        validators=[("RegexValidator", 'r"^\\d{3}-\\d{3}-\\d{4}$"')],
    )
