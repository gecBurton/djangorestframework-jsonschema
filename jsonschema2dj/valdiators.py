"""additional jsonschema validators
"""
from json import load
from typing import Dict, Union, Optional

from django.utils.deconstruct import deconstructible  # type: ignore
from jsonschema import Draft7Validator  # type: ignore
from django.core.exceptions import ValidationError  # type: ignore
from django.utils.translation import gettext_lazy  # type: ignore
from django.core import validators  # type: ignore


@deconstructible
class JSONSchemaValidator(validators.BaseValidator):
    """Bespoke jsonschema validator to be used with the JSONField
    """

    def __init__(self, schema: Dict, definitions: Optional[Union[str, Dict]]=None):
        self.definitions = definitions
        self.schema = schema

    @property
    def validator(self):
        if self.definitions:
            if isinstance(self.definitions, str):
                with open(self.definitions) as f:
                    definitions = load(f).get("definitions")
            else:
                definitions = self.definitions
            return Draft7Validator(dict(definitions=definitions, **self.schema))
        return Draft7Validator(self.schema)

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


@deconstructible
class MultipleOfValidator(validators.BaseValidator):
    message = ('%(value)s is not a multiple of %(factor)')
    code = 'factor'

    def __init__(self, factor, message=None):
        self.factor = factor
        if message:
            self.message = message

    def __call__(self, value):
        if value % self.factor == 0:
            params = {'value': value, 'factor': self.factor}
            raise ValidationError(self.message, code=self.code, params=params)
