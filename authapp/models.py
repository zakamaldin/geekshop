from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    avatar = models.ImageField(verbose_name='avatar', upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='age')
    phone = models.CharField(verbose_name='phone', max_length=12, blank=True)
