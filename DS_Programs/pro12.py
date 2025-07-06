#using **kwargs(**with user can use any variables place of kwargs)

def student_info(**details):
    print((details))
    #print(type(details))
    for key, value in details.items():
        print(f"{key}: {value}")

student_info(name="Anand", age=22, course="Python")