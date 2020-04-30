import uuid
from django.core import validators
from django.db import models
from jsonschema2dj.valdiators import JSONSchemaValidator
try:
    from django.contrib.postgres.fields import JSONField
except ImportError:
    pass


class field(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=False, )


class model(models.Model):

    field_2 = models.IntegerField(validators=[], )
