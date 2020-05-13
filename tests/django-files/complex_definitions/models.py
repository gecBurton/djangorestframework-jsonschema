import uuid
from django.core import validators
from django.db import models
from jsonschema2dj.valdiators import JSONSchemaValidator
try:
    from django.contrib.postgres.fields import JSONField
except ImportError:
    pass
import pathlib

DEFINITIONS = str(pathlib.Path(__file__).parent.absolute() / "schema.json")


class model(models.Model):

    field_2 = models.IntegerField(null=True, validators=[])
    field_1 = JSONField(default = dict, null = True, validators=[JSONSchemaValidator({'$ref': '#/definitions/field'}, DEFINITIONS)])
