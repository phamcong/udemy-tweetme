# inline validation functions for each form field.
# inline validation functions should be in a separated file.
from django.core.exceptions import ValidationError

def validate_content(value):
    content = value
    if content == "abc":
        raise ValidationError("Content cannot be ABC")
    return value
