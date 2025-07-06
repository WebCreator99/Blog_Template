class Human:
    def __init__(self, name="Unknown", age=0, salary=-1):
        self.name = name
        self.age = age
        self.salary = salary

    def walk(self):
        print(f"{self.name} is walking")

c = Human("Chandan", 22, 5)
d = Human("darshan", 20)

paapu = Human()
paapu.name = "Aryan"
paapu.walk()