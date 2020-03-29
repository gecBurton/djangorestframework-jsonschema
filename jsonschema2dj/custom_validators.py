from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_multile_of(value):
    if value % 10 != 0:
        raise ValidationError(
            _('%(value)s is not a multiple of'),
            params={'value': value},
        )
