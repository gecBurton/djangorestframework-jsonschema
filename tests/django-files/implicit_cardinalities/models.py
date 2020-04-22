import uuid
from django.core import validators
from django.db import models

try:
    from jsonschema2dj.extra_fields import ValidatedJSONField
except ImportError:
    pass


class A(models.Model):

    b = models.OneToOneField("B",on_delete=models.CASCADE,)


class B(models.Model):

    a = models.OneToOneField("A",on_delete=models.CASCADE,)
    c = models.ForeignKey("C",on_delete=models.CASCADE,)


class C(models.Model):

    d = models.ForeignKey("D",on_delete=models.CASCADE,)


class D(models.Model):

    e = models.ManyToManyField("E",)


class E(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=False, )
