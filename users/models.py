from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .managers import CustomUserManager
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    fb_login = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_email(self):
        return str(self.email)
