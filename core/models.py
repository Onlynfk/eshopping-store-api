from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# - Create a shopping Store and an Order.

# shoping store


class Status(models.TextChoices):
    OPENED = ("opened",)
    CANCELLED = ("cancelled",)
    DELIVERED = ("delivered ",)
    NULL = ("null ",)


class Categories(models.TextChoices):
    FASHION = ("fashion",)
    COMPUTING = ("computing",)
    ELECTRONICS = ("electronics",)
    GAMING = ("gaming",)
    PHONES = ("phones",)
    AUTOMOBILE = ("automobile ",)






class Product(models.Model):
    """A model that contains data for a single product."""
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    name = models.CharField(max_length=255, help_text="Product Name")
    store = models.ForeignKey('Store', null=True, related_name="add_products", blank=True, on_delete=models.CASCADE)
    available_inventory = models.PositiveIntegerField(default=0)
    category=models.CharField(max_length=50, choices=Categories.choices, default=Categories.COMPUTING)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True )

    def __str__(self):
        return self.name

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    store = models.ForeignKey('Store',null=True, related_name="orders", blank=True, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    state = models.CharField(max_length=50, choices=Status.choices, default=Status.NULL)
    deleted = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Orders'
        verbose_name_plural = 'Orders'
        
    def __str__(self):
        return f"{self.quantity} of {self.item.name}"
    
    def get_total_item_price(self):
        return self.quantity * self.item.price
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """ Adds . """
        if self.state == 'cancelled':
            self.state = 'cancelled'
            self.deleted = True
        super().save(force_insert, force_update, using, update_fields)


class Order(models.Model):
    """
    An Order is the more permanent counterpart of the shopping cart. It represents
    the frozen the state of the cart on the moment of a purchase. In other words,
    an order is a customer purchase.
    """
    customer = models.ForeignKey(User,related_name='orders',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    being_delivered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    received = models.BooleanField(default=False) 
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(auto_now_add=True, blank=True, null=True )
    total_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True )

    class Meta:
        verbose_name = 'User Order Summary'
        verbose_name_plural = 'Users Order Summaries'
        
    def __str__(self):
        return self.customer.username
     
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()
        return total
     


class Store(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    all_orders = models.ManyToManyField(OrderItem, related_name= "placed_orders")
    products = models.ManyToManyField(Product, related_name="products_list")
    name = models.CharField(max_length=255, help_text="Store Name")

    def __str__(self):
        return self.name
