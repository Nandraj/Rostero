from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50, null=True)
    price = models.FloatField()
    opg_stock = models.FloatField()
    image = models.ImageField(upload_to='images/')

    category = models.ForeignKey(
        Category, null=True, on_delete=models.SET_NULL)
