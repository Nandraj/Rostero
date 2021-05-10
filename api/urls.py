from django.urls import path, include
from . import views
from rest_framework import routers
from .api import (
    CategoryViewSet,
    ProductViewSet,
    CustomerViewSet,
    SaleViewSet,
    SaleReturnViewSet,
    SupplierViewSet,
    PurchaseViewSet,
    PurchaseReturnViewSet
)

router = routers.DefaultRouter()
router.register('category', CategoryViewSet, 'category')
router.register('product', ProductViewSet, 'product')
router.register('customer', CustomerViewSet, 'customer')
router.register('sale', SaleViewSet, 'sale')
router.register('salereturn', SaleReturnViewSet, 'salereturn')
router.register('supplier', SupplierViewSet, 'supplier')
router.register('purchase', PurchaseViewSet, 'purchase')
router.register('purchasereturn', PurchaseReturnViewSet, 'purchasereturn')


urlpatterns = [
    path('', views.apiOverview),
    path('', include(router.urls))
]
