from django.contrib.postgres.fields import JSONField
from jsonschema import Draft7Validator
from rest_framework import exceptions
from rest_framework.utils import json


class ValidatedJSONField(JSONField):
    def __init__(self, *args, schema=None, **kwargs):
        self.schema = schema
        super().__init__(*args, **kwargs)

    def validate(self, value, model_instance):
        value = super().validate(value, model_instance)
        data = json.loads(value)
        validator = Draft7Validator(self.schema)
        if errors := list(validator.iter_errors(data)):
            raise exceptions.ValidationError(errors, code="invalid")
        return value
