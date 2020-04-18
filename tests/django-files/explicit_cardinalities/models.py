import uuid
from django.core import validators
from django.db import models

try:
    from extra_fields import JSONSchemaField
except ImportError:
    pass


class A(models.Model):

    b = models.OneToOneField("B", null=True, on_delete=models.CASCADE,)


class B(models.Model):

    a = models.OneToOneField("A", null=True, on_delete=models.CASCADE,)
    c = models.ForeignKey("C", null=True, on_delete=models.CASCADE,)


class C(models.Model):

    d = models.ForeignKey("D", null=True, on_delete=models.CASCADE,)


class D(models.Model):

    e = models.ManyToManyField("E", null=True, on_delete=models.CASCADE,)


class E(models.Model):

    d = models.ManyToManyField("D", null=True, on_delete=models.CASCADE,)
