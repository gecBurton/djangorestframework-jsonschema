from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_multiple_of(value, multiple_of):
    if value % multiple_of != 0:
        raise ValidationError(
            _('%(value)s is not a multiple of'),
            params={'value': value},
        )