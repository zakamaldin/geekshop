from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta


class ShopUser(AbstractUser):
    avatar = models.ImageField(verbose_name='avatar', upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='age', default=18)
    phone = models.CharField(verbose_name='phone', max_length=12, blank=True)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True


class GoogleUserProfile(models.Model):
    account = models.OneToOneField(ShopUser, on_delete=models.CASCADE)


class VkUserProfile(models.Model):
    account = models.OneToOneField(ShopUser, on_delete=models.CASCADE)



