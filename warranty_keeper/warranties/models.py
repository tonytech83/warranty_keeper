from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator

from warranty_keeper.core.model_mixins import TimeStampedModel
from warranty_keeper.warranties.validators import validate_mime_type
from warranty_keeper.suppliers.models import Supplier


UserModel = get_user_model()

class Warranty(TimeStampedModel,models.Model):
    MAX_NAME_LENGTH = 100
    MIN_NAME_LENGTH = 2

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_NAME_LENGTH),
        ),
        unique=False,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    invoice_img = models.FileField(
        upload_to='invoices/',
        validators=(
            validate_mime_type,
        ),
        null=True,
        blank=True,
    )

    owner = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    supplier = models.ForeignKey(
        to=Supplier,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
