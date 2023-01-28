from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from datetime import datetime
from django.db import models
from uuid import uuid4
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .UserManager import CustomUser
class CustomerUsers(AbstractBaseUser, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(_('first name'),max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(_('phone'), unique=True, max_length=50)
    DOB = models.DateTimeField(_('DOB'), default=datetime.now)
    gender = models.CharField(max_length=30, choices=(
        ('M', 'Male'), ('F', 'Female'), ('O', 'Others')
    ))
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateField(default=timezone.now)
    user_updated = models.DateField(default=timezone.now)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    object = CustomUser()

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name_plural = 'CustomUser'