class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age #private attribute

    #Getter for age
    def get_age(self):
        return self.__age

    #setter for  age
    def set_age(self, age):
        if age > 0: #validation
            self.__age = age
        else:
            print("Invalid age")

#usage
student = Student("Anita", 20)
print("Age:", student.get_age())  #accessing age with getter
student.set_age(21) #Modifying age with setter
print("Update Age:", student.get_age())

