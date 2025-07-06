class Animal:
    def sound(self):
        print("This animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

#usage
animal = Animal()
animal.sound()
dog=Dog()
dog.sound()  # calls the overridden in Dog class

