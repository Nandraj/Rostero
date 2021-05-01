from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=50, null=True, unique=True)
    price = models.FloatField()
    opg_stock = models.FloatField(default=0)
    image = models.ImageField(upload_to='products/')

    category = models.ForeignKey(
        Category, null=True, on_delete=models.SET_NULL)
