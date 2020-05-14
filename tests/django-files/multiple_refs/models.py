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


class Patient(models.Model):

    _birthDate = JSONField(default = dict, null = True, validators=[JSONSchemaValidator({'$ref': '#/definitions/Element'}, DEFINITIONS)])
    _deceasedDateTime = JSONField(default = dict, null = True, validators=[JSONSchemaValidator({'$ref': '#/definitions/Element'}, DEFINITIONS)])
