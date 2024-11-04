def validate_positive_integer(value, field_name):
    if not isinstance(value, int) or value < 0:
        raise ValueError(f"{field_name} must be a positive integer.")

def validate_email(email):
    from django.core.validators import validate_email
    try:
        validate_email(email)
    except ValidationError:
        raise ValueError("Invalid email address.")
