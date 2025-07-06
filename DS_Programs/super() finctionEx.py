class Animal:
    def make_sound(self):
        print("This animal makes a sound")

class Dog(Animal): #child
    def make_sound(self):
        super().make_sound()
        print("Bark")

    def get_angry(self):
        super().make_sound() #parent refer
        self.make_sound() #self

#usage
dog=Dog()
dog.get_angry()

