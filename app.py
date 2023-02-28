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
        if (product, quantity) in self.items:
            self.items.remove((product, quantity))
            self.total -= product.price * quantity

    
   # Implement the checkout feature: Create a function that allows the user to check out and complete their purchase. This function should calculate the total price of the cart, apply any applicable discounts or coupons, and generate an order confirmation.
   
   # calculate the total price of the cart after applying discounts and coupons
    def checkout(self):
        total = 0
        for product, quantity in self.items:
            total += product.price * quantity
        total -= self.discount
        total -= self.coupon
        print(f"Thank you for tshopping with us.  Your total is {total}, your confirmation number is 024934782, and your product will ship in 1-3 business days.  Have a great day!")
        
# Save the order history: Save the order history in a database or a file, so that the user can view their past orders.
    def save_order(self):
        with open('order_history.txt', 'a') as f:
            f.write(f"{self.items}, {self.total}, {self.coupon}, {self.discount}")
        
# create instances of the Product class
python_course = Product("Python Programming: An Introduction", "Learn Python from scratch in this beginner's course", 50, 10)
data_science_course = Product("Data Science for Everyone", "A comprehensive guide to data science", 80, 5)

# create an instance of the Cart class
cart = Cart()

# add items to the cart
cart.add_to_cart(python_course, 2)
cart.add_to_cart(data_science_course, 1)

# remove an item from the cart
cart.remove_from_cart(python_course, 1)

# checkout and save the order
cart.checkout()
cart.save_order()
