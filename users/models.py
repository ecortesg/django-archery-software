from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from core.models import AbstractBaseModel
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin, AbstractBaseModel):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(
        default=True,
        help_text="Designates whether the user can log into this admin site.",
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = "user"

    def __str__(self):
        return self.email
