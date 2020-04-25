from jsonschema import Draft7Validator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy


class JSONSchemaValidator:
    def __init__(self, schema):
        self.validator = Draft7Validator(schema)

    def __call__(self, payload):
        if errors := list(self.validator.iter_errors(payload)):
            raise ValidationError(gettext_lazy("%(value) raised"), params={"value": errors})
