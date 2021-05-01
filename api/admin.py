from django.contrib import admin
from .models import (
    Category,
    Product,
    Customer,
    Sale,
    SaleReturn
)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Sale)
admin.site.register(SaleReturn)
