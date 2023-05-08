#List of items a user can buy 
#User input for the items they want 
#Empty Dict so they can keep track of their cart (Quanity Item and Price)
#Option to continue to add/remove from list 
#View cart when they checkout 
#When quit show this: 
#       Your reciept:
#               5 appples x 1.97 = whatever the math
#               6 bananas x 2.21 = whatever you get the point 
#               Total = a shit load with Biden 


def shopping_cart():
    cart = {}
    items = {
        'apples' : 1.25,
        'bananas' : 1.15,
        'bread' : 2.25,
        'rice' : 1.75,
        'yogurt' : 2.50
    }
    print("Hello and welcome to the first ever META SHOPPING MART!!!!!!")
    user_input = input("Would you like to 'enter', or 'go back' into the real world.....\nEnter to go forward, Go Back to exit not case sensitive :)  ")
    user_input = user_input.lower()
    if user_input == "enter":
        print(f"\nA person of culture I see...\nHere is our whole inventory:")
        for item, price in items.items():
            print(f"{item}: {price}")
        want_to_shop = input("\nI know it's not a lot. We are just classic computers after all. \n\t Would you still like to shop? (yes/no or y/n)")
        want_to_shop = want_to_shop.lower()
        while want_to_shop in ['yes', 'y']:
            cart_input = input("What item would you like to add to your cart: ")
            if cart_input in items:
                if cart_input in cart:
                    cart[cart_input]['quantity'] += 1
                else:
                    cart[cart_input] = {'quantity': 1, 'price': items[cart_input]}
                print(f"{cart_input} added to cart!")
            else:
                print(f"Sorry, {cart_input} is not in stock currently.")
            want_to_shop_input = input("Would you like to add more items to your cart? (yes/no or y/n)").lower()
            if want_to_shop_input in ['no', 'n']:
                break

    print("\nHere is your e-reciept")
    total = 0
    for item, details in cart.items():
        print(f"{item}: {details['quantity']} x ${details['price']} = ${details['quantity'] * details['price']:.2f}")
        total += details['quantity'] * details['price']
    print(f"\n Your total is ${total:.2f}")
    print("Thank you for shopping with us! \n\t Don't forget to give a good review on Yelp!")
            


        

shopping_cart()