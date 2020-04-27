"""additional jsonschema validators
"""
from django.utils.deconstruct import deconstructible
from jsonschema import Draft7Validator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from django.core import validators


@deconstructible
class JSONSchemaValidator(validators.BaseValidator):
    """Bespoke jsonschema validator to be used with the JSONField
    """

    def __init__(self, schema):
        self.validator = Draft7Validator(schema)

    def __call__(self, payload):
        if errors := list(self.validator.iter_errors(payload)):
            raise ValidationError(
                [
                    ValidationError(
                        gettext_lazy("JSONSchema: %(value)s"),
                        params={"value": error.message.replace("\\\\", "\\")},
                        code="jsonschema",
                    )
                    for error in errors
                ]
            )
