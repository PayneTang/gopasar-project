from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .managers import CustomUserManager
from django.utils.translation import ugettext_lazy as _
from common.utils import get_avatar_upload_destination

# Create your models here.


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    fb_login = models.BooleanField(default=False)
    google_login = models.BooleanField(default=False)
    phone_number = models.IntegerField(null=True)
    date_of_birth = models.DateField(null=True)
    description = models.TextField(null=True)
    avatar = models.ImageField(
        upload_to=get_avatar_upload_destination, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_email(self):
        return str(self.email)
