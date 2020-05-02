import uuid
from django.core import validators
from django.db import models
from jsonschema2dj.valdiators import JSONSchemaValidator
try:
    from django.contrib.postgres.fields import JSONField
except ImportError:
    pass


class model(models.Model):

    field_1 = JSONField(validators=[JSONSchemaValidator({'$ref': '#/definitions/field'})])
    field_2 = models.IntegerField(validators=[])
