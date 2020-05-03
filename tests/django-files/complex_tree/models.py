import uuid
from django.core import validators
from django.db import models
from jsonschema2dj.valdiators import JSONSchemaValidator
try:
    from django.contrib.postgres.fields import JSONField
except ImportError:
    pass


class Hospital(models.Model):

    postcode = models.CharField(null=True, max_length=255, validators=[validators.RegexValidator("^[a-z]{1,2}\d[a-z\d]?\s*\d[a-z]{2}$")])
    type = models.CharField(null=True, max_length=7, choices=[('general', 'general'), ('local', 'local'), ('clinic', 'clinic')])


class Doctor(models.Model):

    name = models.CharField(null=True, max_length=255)
    hospital = models.ForeignKey("Hospital", null=True, on_delete=models.CASCADE)
    patient = models.ManyToManyField("Patient", null=True)


class Patient(models.Model):

    nhs_number = models.CharField(null=True, max_length=255, validators=[validators.RegexValidator("^\d{3}-\d{3}-\d{4}$")])
