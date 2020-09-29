from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=30)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
