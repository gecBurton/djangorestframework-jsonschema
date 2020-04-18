import uuid
from django.core import validators
from django.db import models

try:
    from extra_fields import JSONSchemaField
except ImportError:
    pass


class F(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=False,)


class E(models.Model):

    f = models.ForeignKey("F", null=True, on_delete=models.CASCADE,)


class D(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=False,)


class C(models.Model):

    d = models.ForeignKey("D", null=True, on_delete=models.CASCADE,)


class B(models.Model):

    c = models.ForeignKey("C", null=True, on_delete=models.CASCADE,)
    e = models.ForeignKey("E", null=True, on_delete=models.CASCADE,)


class A(models.Model):

    b = models.ForeignKey("B", null=True, on_delete=models.CASCADE,)
