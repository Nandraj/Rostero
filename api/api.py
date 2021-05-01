from .models import Category, Product
from rest_framework import viewsets, permissions
from .serializers import (
    CateorySerializer,
    ProductSerializer
)

permission_cls = [
    # TODO: change permission to appropriate value
    permissions.AllowAny
]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = permission_cls
    serializer_class = CateorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = permission_cls
    serializer_class = ProductSerializer
