from django.urls import path
from . import views
from rest_framework import routers
from .api import (
    CategoryViewSet,
    ProductViewSet,
    CustomerViewSet,
    SaleViewSet,
    SaleReturnViewSet
)

router = routers.DefaultRouter()
router.register('category', CategoryViewSet, 'category')
router.register('product', ProductViewSet, 'product')
router.register('customer', CustomerViewSet, 'customer')
router.register('sale', SaleViewSet, 'sale')
router.register('salereturn', SaleReturnViewSet, 'salereturn')


urlpatterns = [
    path('', views.apiOverview)
] + router.urls
