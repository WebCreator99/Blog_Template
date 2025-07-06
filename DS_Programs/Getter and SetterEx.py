class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_name(self, name):
        self.__name = name
    
    def set_age(self, age):
        if isinstance(age, int):  #data type validation check it is int or float, or string.
            self.__age = age
        else:
            print("Age should be an int. ERROR")


student= Student("Chandan", 22)
student.set_age("sjhf")
#print(student.get_name())
#student.set_name("darshan")
#print(student.get_name())
print("Age:", student.get_age())
student.set_age(21)
print("Update Age:", student.get_age())

