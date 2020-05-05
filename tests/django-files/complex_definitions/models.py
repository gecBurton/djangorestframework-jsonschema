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


class model(models.Model):

    field_1 = JSONField(validators=[JSONSchemaValidator({'$ref': '#/definitions/field'}, DEFINITIONS)])
    field_2 = models.IntegerField(null=True, validators=[])
