class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
        
s = Student("Chandan", 22)
print(s.get_name())
s.set_name("darshan")
print(s.get_name())