class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} make a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def sound(self):
        super().sound()
        print(f"{self.name} barks")

# Usage
dog = Dog("Buddy", "Labrador")
dog.sound()