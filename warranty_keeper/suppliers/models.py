from django.db import models

from django.core.validators import MinLengthValidator

from phonenumber_field.modelfields import PhoneNumberField


class Supplier(models.Model):
    MIN_NAME_LENGTH = 2
    MAX_NAME_LENGTH = 50

    MAX_PHONE_LENGTH = 15

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=(MinLengthValidator(MIN_NAME_LENGTH),),
        unique=True,
        null=False,
        blank=False,
    )

    phone_number = PhoneNumberField(
        null=True,
        blank=True,
        unique=True,
        help_text="Please enter a valid phone number, including country code.",
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    website = models.URLField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
