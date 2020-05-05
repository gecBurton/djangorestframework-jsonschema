import uuid
from django.core import validators
from django.db import models
from jsonschema2dj.valdiators import JSONSchemaValidator
try:
    from django.contrib.postgres.fields import JSONField
except ImportError:
    pass
from json import load
with open("schema.json") as f:
    DEFINITIONS = load(f).get("definitions", {})


class A(models.Model):

    b = models.OneToOneField("B", null=True, on_delete=models.CASCADE)


class B(models.Model):

    a = models.OneToOneField("A", null=True, on_delete=models.CASCADE)
    c = models.ForeignKey("C", null=True, on_delete=models.CASCADE)


class C(models.Model):

    d = models.ForeignKey("D", null=True, on_delete=models.CASCADE)


class D(models.Model):

    e = models.ManyToManyField("E", null=True)


class E(models.Model):

    d = models.ManyToManyField("D", null=True)
