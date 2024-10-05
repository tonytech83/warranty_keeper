import mimetypes

from django.core.exceptions import ValidationError

def validate_mime_type(value):
    mime_type, _ = mimetypes.guess_type(value.name)
    allowed_mime_types = ['image/jpeg', 'image/png', 'application/pdf', 'text/plain']

    if mime_type not in allowed_mime_types:
        raise ValidationError('Unsupported file type.')