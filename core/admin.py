from django.contrib import admin

from .models import Order, OrderItem, Product, Store


class OrderItemAdmin(admin.ModelAdmin):
    readonly_fields = ('deleted','ordered','quantity','item','store')


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('customer','created_at','updated_at','being_delivered','items','total_price')


# Register your models here.
admin.site.register(Store)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Product)
