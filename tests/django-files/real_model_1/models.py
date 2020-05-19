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


class Sample(models.Model):

    sample_id = models.IntegerField(validators=[])
    well = models.CharField(max_length=255, validators=[validators.RegexValidator('^[1-9][A-C]$')])
    percentage = models.DecimalField(null=True, validators=[validators.MinValueValidator(-10), validators.MaxValueValidator(100.0)], max_digits=10, decimal_places=5)
    hazaradous = models.CharField(null=True, max_length=3, choices=[('yes', 'yes'), ('no', 'no')])
    type = models.CharField(null=True, max_length=6, choices=[('blood', 'blood'), ('saliva', 'saliva'), ('tumour', 'tumour')])
    _class = models.ForeignKey("Rack", null=True, verbose_name="class", on_delete=models.CASCADE)
    patient = models.ManyToManyField("Patient", null=True)


class Patient(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    sex = models.CharField(max_length=2, choices=[('xx', 'XX'), ('xy', 'XY')])
    nhs_number = models.CharField(max_length=255, validators=[validators.RegexValidator('^\d{3}-\d{3}-\d{4}$')])
    DOB = models.DateField(null=True)
    clinic = models.CharField(null=True, max_length=255)
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE)


class Doctor(models.Model):

    name = models.CharField(null=True, max_length=255)
    email = models.EmailField(null=True)
    address = JSONField(default=dict, null=True, validators=[JSONSchemaValidator({'$ref': '#/definitions/address'}, DEFINITIONS)])


class Rack(models.Model):

    id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=255, validators=[validators.RegexValidator('^[A-D][0-9]{4}-[0-9]{5}$')])
    delivery_type = models.CharField(null=True, max_length=7, choices=[('courier', 'courier'), ('manual', 'manual')])
