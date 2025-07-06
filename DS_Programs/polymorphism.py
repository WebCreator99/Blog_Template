class Animal:
    def make_sound(self):
        print("Animal is making sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

animals = [Dog(), Cat()]
for animal in animals:
    animal.make_sound()