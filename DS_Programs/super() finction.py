class Animal:
    def make_sound(self):
        print("This animal makes a sound")

class Dog(Animal): #child
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        super().make_sound()
        print(f"{self.name} is Barking")

#usage
dog=Dog("doggy")
dog.make_sound()  # calls the overridden in Dog class

