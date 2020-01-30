from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,\
                                       PermissionMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        user = self.mode(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
  