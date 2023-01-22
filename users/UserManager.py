from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUser(BaseUserManager):

    def create_user(self, email, password, **extra_field):
        if not email:
            raise ValueError(_('Email is required'))
        email = self.normalize_email(email)
        user  = self.model(email=email, **extra_field)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_field):
        """
            Create and save a SuperUser with a given email and password.
        """
        extra_field.setdefault('is_staff', True)
        extra_field.setdefault('is_superuser', True)
        extra_field.setdefault('is_active', True)

        if extra_field.get('is_staff') is not True:
            raise ValueError(_('SuperUser must have is_staff=True'))
        if extra_field.get('is_superuser') is not True:
            raise ValueError(_('SuperUser must have is_superuser=True'))
        if extra_field.get('is_active') is not True:
            raise ValueError(_('SuperUser must have is_active=True'))
        return self.create_user(email, password, **extra_field)