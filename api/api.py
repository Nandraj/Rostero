from .models import (
    Category,
    Product,
    Customer,
    Sale,
    SaleReturn
)
from rest_framework import viewsets, permissions
from .serializers import (
    CateorySerializer,
    ProductSerializer,
    CustomerSerializer,
    SaleSerializer,
    SaleReturnSerializer
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


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    permission_classes = permission_cls
    serializer_class = CustomerSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    permission_classes = permission_cls
    serializer_class = SaleSerializer


class SaleReturnViewSet(viewsets.ModelViewSet):
    queryset = SaleReturn.objects.all()
    permission_classes = permission_cls
    serializer_class = SaleReturnSerializer
