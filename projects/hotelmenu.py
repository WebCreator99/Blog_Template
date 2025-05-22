#Define menu of restaurant

menu = {
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80,
}

#Greet
print(" Welcome to our restaruant")
print(" Pizza:40\n Pasta:50\n Burger:60\n Salad:70\n Coffee:80\n")

order_total = 0
#80 + 70 =150

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
    
else:
    print(f"Oreder item{item_1} is not available yet!")
    
another_order = input("Do you want to add another item? (YES/NO) ")
if another_order == "YES":
    item_2 = input("Enter the name of second item = ")
    if item_2  in menu:
        order_total += menu[item_2]
    else:
        print(f"Ordered item {item_2} is not available!")
print(f"The total amount of items to pay is {order_total}")
    