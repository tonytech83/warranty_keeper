from django.db import models

from django.contrib.auth import models as auth_models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator

from warranty_keeper.accounts.validators import check_name_symbols_for_non_alphabetical
from warranty_keeper.accounts.managers import WarrantyKeeperUserManager




class WarrantyKeeperUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
        help_text=_("Provide a valid email address."),
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    
    is_superuser = models.BooleanField(
        _("superuser status"),
        default=False,
        help_text=_("Designates whether this user has all permissions without explicitly assigning them."),
    )

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='warranty_keeper_users',
        blank=True,
        help_text=_('The groups this user belongs to.'),
        verbose_name=_('groups'),
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='warranty_keeper_users',
        blank=True,
        help_text=_('Specific permissions for this user.'),
        verbose_name=_('user permissions'),
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = WarrantyKeeperUserManager()

    def __str__(self) -> str:
        return self.email

class Profile(models.Model):
    MIN_NAME_LENGTH = 2
    MAX_NAME_LENGTH = 15

    first_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_NAME_LENGTH),
            check_name_symbols_for_non_alphabetical,
        ),
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_NAME_LENGTH),
            check_name_symbols_for_non_alphabetical,
        ),
        null=True,
        blank=True,
    )


    account = models.OneToOneField(
        to=WarrantyKeeperUser,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='profile',
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'

        return 'Unknown'

    @property
    def initials(self):
        if self.first_name and self.last_name:
            return f'{self.first_name[0]}{self.last_name[0]}'.upper()

        return self.account.email[0].upper()
