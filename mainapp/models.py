from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True, default='placeholder.png')
    short_desc = models.CharField(verbose_name='кратко', max_length=60, blank=True)
    description = models.TextField(verbose_name='подробно', blank=True)
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='склад', default=0)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.category.name)


