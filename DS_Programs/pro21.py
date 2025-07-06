class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_info(self):
        print(f"Laptop Brand: {self.brand}, Price: {self.price}")

Laptop1 = Laptop("Dell",45000)
Laptop2 = Laptop("HP" , 55000)

Laptop1.show_info()
Laptop2.show_info()