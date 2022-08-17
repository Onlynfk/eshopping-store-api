from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StoreSerializer,ProductSerializer, OrderSerializer,StoreOrdersSerializer,OrderItemSerializer
from .models import Order, OrderItem, Product, Store
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from django.utils import timezone


class CreateStoreViewSet(APIView):
    """
    A viewset for viewing and editing store instances.
    """
    def post(self, request):
        data = request.data
        user = request.user
        store_name = data.get("name")
        if store_name is not None: 
            store = Store.objects.create(
                owner = user,
                name= store_name
            )
            store.save()
            serializer = StoreSerializer(store, many=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(('GET',))
def list_stores(request):
    stores = Store.objects.all()
    serializer = StoreSerializer(stores, many=True)
    return Response(serializer.data)

@api_view(('GET',))
def list_stores(request):
    stores = Store.objects.all()
    serializer = StoreSerializer(stores, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def store_detials(request, pk):
    store = get_object_or_404(Store, pk=pk)
    serializer = StoreSerializer(store, many=False)
    return Response(serializer.data)


@api_view(('GET',))
def all_store_orders(request, pk):
    store = get_object_or_404(Store, pk=pk)
    serializer = StoreOrdersSerializer(store, many=False)
    return Response(serializer.data)



@api_view(('GET',))
def order_details(request, pk):
    order = get_object_or_404(OrderItem, pk=pk)
    serializer = OrderItemSerializer(order, many=False)
    return Response(serializer.data)

@api_view(('PATCH',))
def order_update(request, pk):
    order = get_object_or_404(OrderItem, pk=pk)
    data = request.data
    state = data.get("state")
    order.state = state
    order.save()
    serializer = OrderItemSerializer(order, many=False)
    return Response(serializer.data)


@api_view(('GET',))
def user_order_list(request):
    order = Order.objects.filter(customer=request.user)
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def all_orders(request):
    orders = OrderItem.objects.all()
    serializer = OrderItemSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(('GET',))
def checkout(request):
    order = Order.objects.filter(ordered=False)
    if order.exists():
        orders = order[0]
        length = orders.items.count()
        if length > 0 :
            orders.ordered = True
            orders.save()
            for placed_orders in orders.items.all():
                placed_orders.state = "opened"
                placed_orders.ordered = True
                placed_orders.save()
                store = Store.objects.filter(pk=placed_orders.store.id).first()
                store.all_orders.add(placed_orders)
                store.save()
            serializer = OrderSerializer(orders, many=False)
            return Response(serializer.data)
        message = {'message': 'You do not have Items in your order'}
        return Response(status=404, data=message)
    else:
        message = {'message': 'You do not have an active order'}
        return Response(status=404, data=message) 



@api_view(('GET',))
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(('GET',))
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(('POST',))
def create_product(request):
    data = request.data
    user = request.user
    product_name = data.get("name")
    product_price = data.get("price")
    store_id = data.get("store")
    
    
    product = Product.objects.create(
        owner=user,
        price=product_price,
        name= product_name,
        store_id=store
    )
    product.save()
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(('GET',))
def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False,
        store=item.store

    )
    order_qs = Order.objects.filter(customer=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(pk=item.pk).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
        serializer = OrderSerializer(order, many=False)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            customer=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        serializer = OrderSerializer(order, many=False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    

@api_view(('GET',))
def remove_single_item_from_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(
        customer=request.user,
        ordered=False,
    )
    
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(pk=item.pk).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            serializer = OrderSerializer(order, many=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            message = {'message': 'This item was not in your cart'}
            return Response(status=404, data=message) 
        message = {'message': 'You do not have an active order'}
        return Response(status=status.HTTP_204_NO_CONTENT, data=message) 


