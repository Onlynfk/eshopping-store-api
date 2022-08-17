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












