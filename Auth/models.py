from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from .managers import MyUserManager


# Create your models here.

class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name="Почта пользователя")
    name = models.CharField(max_length=30, blank=True, verbose_name="Имя пользователя")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")
    is_active = models.BooleanField( default=True)
    is_staff = models.BooleanField(default=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'Пользователь с именем {self.name}, почтой {self.email}'
