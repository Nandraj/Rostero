from rest_framework import serializers
from .models import (
    Category,
    Product,
    Customer,
    Sale,
    SaleReturn
)


class CateorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'


class SaleReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleReturn
        fields = '__all__'
