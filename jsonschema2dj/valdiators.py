"""additional jsonschema validators
"""
from django.utils.deconstruct import deconstructible  # type: ignore
from jsonschema import Draft7Validator  # type: ignore
from django.core.exceptions import ValidationError  # type: ignore
from django.utils.translation import gettext_lazy  # type: ignore
from django.core import validators  # type: ignore


@deconstructible
class JSONSchemaValidator(validators.BaseValidator):
    """Bespoke jsonschema validator to be used with the JSONField
    """

    def __init__(self, schema):
        self.validator = Draft7Validator(schema)

    def __call__(self, payload):
        errors = list(self.validator.iter_errors(payload))
        if errors:
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
