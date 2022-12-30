from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager

class ManageUser(BaseUserManager):
    def createUser(self,email,password,**extrafields):
        """
            Creating Common User
        """
        if not email:
            raise ValueError(_('Email is required'))
        email = self.normalize_email(email)
        user = self.model(email, password, **extrafields)
        user.set_password(password)
        user.save()
        return user

    def createSuperUser(self, email, password, **extrafields):
        """
            Creating Super User
        """
        extrafields.setdefault('is_staff', True)
        extrafields.setdefault('is_superuser', True)
        extrafields.setdefault('is_active', True)

        if extrafields.get('is_staff') is not True:
            raise ValueError(_('SuperUser must have is_staff True'))
        
        if extrafields.get('is_super') is not True:
            raise ValueError(_('SuperUser must have is_superuser True'))
        return self.createUser(email, password, **extrafields)