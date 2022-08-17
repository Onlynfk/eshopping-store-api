# ESHopping-store-api

## Live Site : https://eshop23.herokuapp.com

## Installation (Running) Locally
```sh

$ git clone https://github.com/Onlynfk/django-immunization-managment-system.git

$ pipenv shell

$ pip install -r requirements.txt

$ python manage.py makemigrations

$ python manage.py migrate


## Features
- user login
- create a shopping store
- fetch list of store
- fetch specific store
- add a product(item)
- get a product
- list all products
- add product to an order
- remove product from an order
- fetch all orders
- fetch specific order
- fetch a store orders
- update state of an order
- admin can update state of an order via admin site
- cancelled order  sets the deleted order field to true
- admin cannot alter an order fields except order stata
- more .. etc


## Further Improvements
*  Fully functional User Authentication with User Profile
*  Fully functional User Cart System.
*  Some of the logic in the API views should be decomped to model methods.
*  Billing information should be added to the Order model.
*  full CRUD endpoints for both Order and Product model.
*  More in depth unit testing on orders.
*  Restrict permission to update orders to only the creator(user) and admin.
*  Run few background tasks using celery and redis
*  An endpoint to let store owners add products to their store directly
* and more.. 

### API ENDPOINTS 
START_URL = https://eshop23.herokuapp.com

### Store Endpoints

METHOD: POST
Desc: Create a Store
URL - {{START_URL}}/store/create/


METHOD: GET
Desc: List Stores
URL - {{START_URL}}/store/

METHOD: 
Desc: Get a  Store
URL - {{START_URL}}/store/<store_id>/

METHOD: 
Desc: Get a Store Orders
URL - {{START_URL}}/store/<store_id>/orders/


### Products(Items) Endpoints

METHOD: POST
Desc: Create a Product
URL - {{START_URL}}/product/create/


METHOD: GET
Desc: Get a Product
URL - {{START_URL}}/product/<product_id>/

METHOD: GET
Desc: List all Products
URL - {{START_URL}}/products/


### Adding a Product(Item) to an Order / Creating an Order
Hint: if product is in order already then it increases just the product quantity or adds a new the product if not
 
METHOD: GET
Desc: Add Product to an order
URL - {{START_URL}}/add-to-cart/<product_id>/

### Removing/Updating a Product(Item) to an Order
 Hint: if product is in order already then it decreases just the quantity

METHOD: GET
Desc: Remove Product to an order
URL - {{START_URL}}/remove-to-cart/<product_id>/


### View all orders
METHOD: GET
Desc: List Orders
URL - {{START_URL}}/orders/



### Get Current user Order
METHOD: GET
Desc: View an Order details
URL - {{START_URL}}/orders/me/



### View a Single Order
METHOD: GET
Desc: View an Order details
URL - {{START_URL}}/orders/<order_id>/


### Update an Order
Hint: an order state can be updated
METHOD: GET
Desc: Update an order
URL - {{START_URL}}/orders/<order_id>/

### Checkout your order 
Hint: needed to only send to send orders checkout to store owners

METHOD: GET
Desc: Checkout Order
URL - {{START_URL}}/checkout/











































