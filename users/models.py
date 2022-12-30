from django.db import models
from datetime import datetime
from django.utils import timezone
from uuid import uuid4
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from . manageUsers import ManageUser

def upload_to(instance, filename):
    return f"images/{filename}".format(filename)

# Create your models here.
class customerUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    profile = models.ImageField(upload_to=upload_to, default='/img/beers.jpg')
    firstName = models.CharField(_('firstName'),max_length=70)
    lastName = models.CharField(_('lastName'),max_length=70)
    email = models.EmailField(_('email'),unique=True)
    phone = models.CharField(_('phone'),max_length=50)
    gender = models.CharField(max_length=30, choices=(
        ('M', 'Male'), ('F', 'Female'), ('O', 'Others')
    ))
    dob = models.DateField(_('DOB'),default=datetime.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateField(default=timezone.now)
    user_updated = models.DateField(default=timezone.now)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = ManageUser()

    def __str__(self):
        return self.email

    
