print("==============WELCOME TO DRINKS.CO===================")
name = input("Enter your name: ")
menu = "champagne, wine, tea, coffee, juice, milkshake, yoghurt."
flavour = "strawberry, vanilla."
order = input(f"Hello {name}, what would u like to order from our menu:\n {menu} ")
quantity = float(input(f"How many glasses of {order} would you like: "))
if order.lower() == "champagne" :
    price = 200
elif order.lower() == "wine" :
    price =150
elif order.lower() == "tea" :
    price = 50    
elif order.lower() == "coffee" :
    price = 100
elif order.lower() == "juice" :
    price = 70     
elif order.lower() == "milkshake" :
    price = 120
elif order.lower() == "yoghurt" :
    price = 50
else:
    print(f"Sorry {name}. We don't have {order} here") 
    quit()           
cost = price * quantity
print(f"Please wait to be served. You will pay ${cost} at the counter.")    
