from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    UserManager,
    PermissionsMixin
)


class UserManager(UserManager):

    def create_superuser(self, email, password):
        if email is None:
            raise TypeError("email field cannot be empty. ")
        if password is None:
            raise TypeError("Please enter password. ")

        user = self.create_user(email=email, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

    def create_user(self, email, password=None):
        if email is None:
            raise TypeError("Email field cannot be empty. ")

        user = self.model(email=email)
        user.set_password(password)
        user.save()

        return user


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=255, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    

    objects = UserManager()

    def __str__(self):
        return self.username