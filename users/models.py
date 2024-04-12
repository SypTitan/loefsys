from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    #is_active = models.BooleanField(default=True)
    #date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

class Contact(models.Model):
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        null=True,
    )
    #tel
    #mail
    #iban
    #other relevant contact info

    def __str__(self):
        return f"Contact information for {self.user.get_username()}"