from django.db import models
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_date = models.DateTimeField(default=now, editable=False)

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

    created_date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pinzip = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    created_date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.name


class Sale(models.Model):
    date = models.DateTimeField()
    ref = models.CharField(max_length=50, null=True)
    qty = models.FloatField()
    price = models.FloatField()
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(
        Product, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.id)


class SaleReturn(models.Model):
    date = models.DateTimeField()
    ref = models.CharField(max_length=50, null=True)
    qty = models.FloatField()
    price = models.FloatField()
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(
        Product, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.id)


class Supplier(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pinzip = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    created_date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    date = models.DateTimeField()
    ref = models.CharField(max_length=50, null=True)
    qty = models.FloatField()
    price = models.FloatField()
    supplier = models.ForeignKey(
        Supplier, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(
        Product, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.id)


class PurchaseReturn(models.Model):
    date = models.DateTimeField()
    ref = models.CharField(max_length=50, null=True)
    qty = models.FloatField()
    price = models.FloatField()
    supplier = models.ForeignKey(
        Supplier, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(
        Product, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.id)
