from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class MyUser(AbstractUser):
    name = models.CharField(max_length=30, blank=True, verbose_name="Имя пользователя")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")
    is_staff = models.BooleanField(default=True)
    is_cooker = models.BooleanField(verbose_name="Повар",
                                    help_text="Выберите данный пункт для того, чтобы данный пользовтель стал поваром",
                                    null=True)
