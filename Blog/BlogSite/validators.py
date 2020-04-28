from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_file_extension(value):
    valid_extentions = ['.pdf']

    value_ext = value.name[value.name.rfind('.'):]

    if value_ext not in valid_extentions:
        raise ValidationError('Unsupported file extention')