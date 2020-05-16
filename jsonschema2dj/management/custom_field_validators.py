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
        if isinstance(self.factor, float):
            quotient = value / self.factor
            failed = int(quotient) != quotient
        else:
            failed = value % self.factor
        if failed:
            params = {'value': value, 'factor': self.factor}
            raise ValidationError(self.message, code=self.code, params=params)
