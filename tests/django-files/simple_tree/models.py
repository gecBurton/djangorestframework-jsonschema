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

    b = models.ForeignKey("B", null=True, on_delete=models.CASCADE)


class B(models.Model):

    c = models.ForeignKey("C", null=True, on_delete=models.CASCADE)
    e = models.ForeignKey("E", null=True, on_delete=models.CASCADE)


class C(models.Model):

    d = models.ForeignKey("D", null=True, on_delete=models.CASCADE)


class D(models.Model):

    id = models.UUIDField(default=uuid.uuid4)


class E(models.Model):

    f = models.ForeignKey("F", null=True, on_delete=models.CASCADE)


class F(models.Model):

    id = models.UUIDField(default=uuid.uuid4)
