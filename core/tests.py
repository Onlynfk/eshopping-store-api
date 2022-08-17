from django.test import TestCase
from .models import Store, Product
# Create your tests here.
class StoreModelTestcase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Store.objects.create(name="Tecno")

    def test_string_method(self):
        store = Store.objects.get(name="Tecno")
        expected_string = f"{store.name}"
        self.assertEqual(str(store), expected_string)

class ProductModelTestcase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(name="Visa", price="1.34")

    def test_string_method(self):
        product = Product.objects.get(name="Visa")
        expected_string = f"{product.name}"
        self.assertEqual(str(product), expected_string)
