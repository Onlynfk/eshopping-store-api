
from rest_framework import serializers
from .models import Order, OrderItem, Product, Store

   
class OrderItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  OrderItem
        fields = ['id', 'store', 'ordered', 'state','quantity']



class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id','name', 'owner', 'date_created', 'all_orders']

class StoreOrdersSerializer(serializers.ModelSerializer):
    orders = OrderItemSerializer(read_only=True, many=True)
    class Meta:
        model = Store
        fields = ['orders']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name', 'owner', 'price','date_created']
        
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Order
        fields = ['id','customer', 'items', 'received','created_at', 'ordered', 'ordered_date']

