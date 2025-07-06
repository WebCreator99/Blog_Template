class Animal:
    def make_sound(self):
        print("This animal makes a sound")

class Dog(Animal): #child
    def make_sound(self):
        super().make_sound()
        print("Bark")

    
#usage
dog=Dog()
dog.make_sound() 

