from rest_framework import routers
from .views import( CreateStoreViewSet, list_stores, store_detials,
                   add_to_cart,remove_single_item_from_cart,all_orders,user_order_list,
                   order_details,checkout,
                   create_product,product_list,product_detail)
from django.urls import path, include

urlpatterns = [
    path('store/create/',CreateStoreViewSet.as_view(), name="create-store"),  
    path('store/', list_stores, name="list-store"),  
    path('store/<int:pk>/',store_detials, name="detail-store"),  
    path('product/create/',create_product, name="create-product"),  
    path('products/',product_list, name="list-product"), 
    path('product/<int:pk>/',product_detail, name="detail-product"),
    

    path('add-to-cart/<int:pk>/', add_to_cart, name='add-to-cart'),
    path('remove-to-cart/<int:pk>/', remove_single_item_from_cart, name='add-to-cart'),

    path('orders/<int:pk>/', order_details, name='detail-order'),
    path('orders/', all_orders, name='list-orders'),
    path('orders/me/', user_order_list, name='user-orders'),
    

    path('checkout/', checkout, name='list-orders'),


] 