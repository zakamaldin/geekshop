from django.db import models

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(
        'authapp.ShopUser',
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    is_active = models.BooleanField(
        default=False
    )

    def __str__(self):
        full_name = self.user.get_full_name()
        title = full_name if full_name else self.user.username
        return f'{title} {self.created.strftime("%Y-%m-%d %H:%M")}'


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='item'
    )
    product = models.ForeignKey(
        'mainapp.Product',
        on_delete=models.CASCADE
    )
    value = models.IntegerField()

    def __str__(self):
        return self.product.name
