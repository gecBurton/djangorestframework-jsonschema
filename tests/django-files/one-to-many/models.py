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


class PatientContact(models.Model):

    gender = models.CharField(null=True, max_length=6, choices=[('male', 'male'), ('female', 'female')])
    patient = models.ForeignKey("Patient", null=True, on_delete=models.CASCADE)


class Patient(models.Model):

    birthDate = models.DateField(null=True)
