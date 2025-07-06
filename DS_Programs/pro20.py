class Human:
    def __init__(self, name, age):
        print("Constructor is called",name)
        print("Constructor is called",age)
        self.name = name
        self.age = age

    def walk(self):
        print(f"{self.name} is walking")
        print(f"{self.age} years old")
       
c = Human("Chandan", 22 )
d = Human("darsan", 20)

d.walk()
c.walk()


print(c.name)
print(c.age)
print(d.name)
print(d.age)


person1 =Human("Arjun",22)
person1.walk()

Human.walk(d)
Human.walk(c)