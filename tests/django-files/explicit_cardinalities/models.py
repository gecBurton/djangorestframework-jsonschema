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


class A(models.Model):

    b = models.OneToOneField("B", null=True, on_delete=models.CASCADE)


class B(models.Model):

    a = models.OneToOneField("A", null=True, on_delete=models.CASCADE)
    c = models.ForeignKey("C", null=True, on_delete=models.CASCADE)


class C(models.Model):

    b = JSONField(validators=[JSONSchemaValidator({'type': 'array', 'items': {'$ref': '#/definitions/B'}}, DEFINITIONS)])
    d = models.ForeignKey("D", null=True, on_delete=models.CASCADE)


class D(models.Model):

    c = JSONField(validators=[JSONSchemaValidator({'type': 'array', 'items': {'$ref': '#/definitions/C'}}, DEFINITIONS)])
    e = models.ManyToManyField("E", null=True)


class E(models.Model):

    d = models.ManyToManyField("D", null=True)
