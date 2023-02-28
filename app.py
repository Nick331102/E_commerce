import csv

class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

# Cart class to keep track of the products in the cart, total price, coupon, and discount        
class Cart:
    def __init__(self):
        self.items = []
        self.total = 0
        self.coupon = 0
        self.discount = 0

    # add items to cart and calculate total price   
    def add_to_cart(self, product, quantity):
        self.items.append((product, quantity))
        self.total += product.price * quantity
        
    # remove items from cart and calculate total price
    def remove_from_cart(self, product, quantity):
        self.items.remove((product, quantity))
        self.total -= product.price * quantity
    
    # display available products and allow user to choose items to add to cart
    def choose_items(self):
        with open('products.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader) # skip header row
            for i, row in enumerate(reader):
                print(f"{i+1}. {row[0]} - {row[1]} - ${row[2]}")
                
            while True:
                choice = input("Enter the number of the product you would like to add to your cart (or 'done' to finish): ")
                if choice == 'done':
                    break
                try:
                    choice = int(choice)
                    if choice < 1 or choice > i+1:
                        print("Invalid choice. Please try again.")
                        continue
                    product = self.get_product(choice)
                    quantity = input("Enter the quantity: ")
                    quantity = int(quantity)
                    self.add_to_cart(product, quantity)
                    print(f"{quantity} {product.name}(s) added to cart.")
                except ValueError:
                    print("Invalid choice. Please try again.")
                    continue

    
                    
   # Implement the checkout feature: Create a function that allows the user to check out and complete their purchase. This function should calculate the total price of the cart, apply any applicable discounts or coupons, and generate an order confirmation.
   
   # calculate the total price of the cart after applying discounts and coupons
    def checkout(self):
        total = 0
        for product, quantity in self.items:
            total += product.price * quantity
        total -= self.discount
        total -= self.coupon
        print(f"Thank you for shopping with us. Your total is ${total:.2f}. Your confirmation number is 024934782, and your product will ship in 1-3 business days. Have a great day!")
        
# Save the order history: Save the order history in a database or a file, so that the user can view their past orders.
    def save_order(self):
        with open('order_history.txt', 'a') as f:
            f.write(f"{self.items}, {self.total}, {self.coupon}, {self.discount}")
        

# create an empty list to hold products
products = []

# read products from the CSV file and append to the list
with open('products.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        products.append(Product(row['product_name'], row['description'], float(row['price']), int(row['quantity'])))

# print the list of products to the user
print("Welcome to our store! Here are the products available for purchase:")
for i, product in enumerate(products):
    print(f"{i+1}. {product.name} - {product.description} - ${product.price}")

cart = Cart()

# prompt the user to select a product and quantity to add to the cart
while True:
    try:
        product_index = int(input("Enter the number of the product you want to add to your cart (or 0 to exit): "))
        if product_index == 0:
            break
        product = products[product_index-1]
        quantity = int(input("Enter the quantity: "))
        cart.add_to_cart(product, quantity)
        print(f"{quantity} {product.name} added to cart.")
    except (ValueError, IndexError):
        print("Invalid input. Please try again.")

# print the items in the cart
print("Items in cart:")
for product, quantity in cart.items:
    print(f"{product.name} - {product.description} - ${product.price} - Quantity: {quantity}")

# prompt the user to select a product and quantity to remove from the cart
while True:
    try:
        product_index = int(input("Enter the number of the product you want to remove from your cart (or 0 to exit): "))
        if product_index == 0:
            break
        product, quantity = cart.items[product_index-1]
        cart.remove_from_cart(product, quantity)
        print(f"{quantity} {product.name} removed from cart.")
    except (ValueError, IndexError):
        print("Invalid input. Please try again.")

# checkout and save the order

cart.checkout()
cart.save_order()

