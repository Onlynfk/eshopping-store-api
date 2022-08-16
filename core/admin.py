from django.contrib import admin

from .models import Order, OrderItem, Product, Store

# Register your models here.
admin.site.register(Store)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product)
