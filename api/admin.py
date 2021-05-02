from django.contrib import admin
from .models import (
    Category,
    Product,
    Customer,
    Sale,
    SaleReturn,
    Supplier,
    Purchase,
    PurchaseReturn
)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Sale)
admin.site.register(SaleReturn)
admin.site.register(Supplier)
admin.site.register(Purchase)
admin.site.register(PurchaseReturn)
