import uuid
from django.core import validators
from django.db import models
from jsonschema2dj.extra_fields import JSONSchemaValidator
try:
    from django.contrib.postgres.fields import JSONField
except ImportError:
    pass


class F(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=False, )


class E(models.Model):

    f = models.ForeignKey("F",on_delete=models.CASCADE,)


class D(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=False, )


class C(models.Model):

    d = models.ForeignKey("D",on_delete=models.CASCADE,)


class B(models.Model):

    c = models.ForeignKey("C",on_delete=models.CASCADE,)
    e = models.ForeignKey("E",on_delete=models.CASCADE,)


class A(models.Model):

    b = models.ForeignKey("B",on_delete=models.CASCADE,)
