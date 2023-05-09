# Create a class called cart that retains items and has methods to add, remove, and show

class ShoppingCart:
    def __init__(self):
        self.cart = {}
        self.items = {
            'apples': 1.25,
            'bananas': 1.15,
            'bread': 2.25,
            'rice': 1.75,
            'yogurt': 2.50
        }

    def display_items_for_sale(self):
        print("\nHere are the items we have for sale:")
        for item, price in self.items.items():
            print(f"{item}: ${price:.2f}")
        print()

    def add_to_cart(self, item):
        if item in self.items:
            if item in self.cart:
                self.cart[item]['quantity'] += 1
            else:
                self.cart[item] = {'quantity': 1, 'price': self.items[item]}
            print(f"{item} added to cart!")
        else:
            print(f"Sorry, {item} is not in stock currently.")

    def remove_from_cart(self, item):
        if item in self.cart:
            self.cart[item]['quantity'] -= 1
            if self.cart[item]['quantity'] == 0:
                del self.cart[item]
            print(f"{item} removed from cart!")
        else:
            print(f"{item} is not in your cart.")

    def display_cart(self):
        print("\nHere are the items in your cart:")
        for item, details in self.cart.items():
            print(f"{item}: {details['quantity']} x ${details['price']} = ${details['quantity'] * details['price']:.2f}")
        print()

    def checkout(self):
        print("\nHere is your e-receipt:")
        total = 0
        for item, details in self.cart.items():
            print(f"{item}: {details['quantity']} x ${details['price']} = ${details['quantity'] * details['price']:.2f}")
            total += details['quantity'] * details['price']
        print(f"\nYour total is ${total:.2f}")
        print("Thank you for shopping with us!\nDon't forget to give a good review on Yelp!")
        self.cart = {}

    def start_shopping(self):
        print("Hello and welcome to the first ever META SHOPPING MART!!!!!!")
        while True:
            user_input = input("\nEnter '1' to display items for sale\nEnter '2' to add an item to your cart\nEnter '3' to remove an item from your cart\nEnter '4' to display your cart\nEnter '5' to checkout\nEnter '6' to exit\n")
            if user_input == '1':
                self.display_items_for_sale()
            elif user_input == '2':
                item = input("What item would you like to add to your cart: ")
                self.add_to_cart(item)
            elif user_input == '3':
                item = input("What item would you like to remove from your cart: ")
                self.remove_from_cart(item)
            elif user_input == '4':
                self.display_cart()
            elif user_input == '5':
                self.checkout()
            elif user_input == '6':
                break
            else:
                print("Invalid input, please try again.")

cart = ShoppingCart()
cart.start_shopping()


#works in VS Code
