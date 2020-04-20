import uuid
from django.core import validators
from django.db import models

try:
    from extra_fields import JSONSchemaField
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

    e = models.ManyToManyField("E",on_delete=models.CASCADE,)


class E(models.Model):

    d = models.ManyToManyField("D",on_delete=models.CASCADE,)
