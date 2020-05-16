from symbol import factor

from django.core.exceptions import ValidationError
from django.core import validators


class MultipleOfValidator(validators.BaseValidator):
    message = _('%(value)s is not a multiple of %(factor)')
    code = 'factor'

    def __init__(self, factor, message=None):
        self.factor = factor
        if message:
            self.message = message

    def __call__(self, value):

        if isinstance(factor, float):
            quotient = value / factor
            failed = int(quotient) != quotient
        else:
            failed = value % factor
        if failed:
            params = {'value': value, 'factor': factor}
            raise ValidationError(self.message, code=self.code, params=params)
