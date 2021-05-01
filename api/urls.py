from django.urls import path
from . import views
from rest_framework import routers
from .api import CategoryViewSet, ProductViewSet


router = routers.DefaultRouter()
router.register('category', CategoryViewSet, 'category')
router.register('product', ProductViewSet, 'product')


urlpatterns = [
    path('', views.apiOverview)
] + router.urls
