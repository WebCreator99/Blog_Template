def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

a = 10
b = 20
#print(add(a,b))
#print(sub(a,b))
#print(mul(a,b))
#print(div(a,b))

def Display_menu():
    print(" ### simple calculater ###")
    print("1. Add\n2. Subtract\n3. Multiplication\n4. Division\n5. Quite")
    #print("2. Subtract")
    #print("3. Multiplication")
    #print("4. Division")
    #print("5. Quit")

while(True):
    
    choice = int(input("Enter your choice: "))

    if choice in {1,2,3}:
        a = int(input("Enter first number: "))
        b = int(input("Enter first number: "))
    
#elif choice==2:
    #a = int(input("Enter first number: "))
    #b = int(input("Enter first number: "))
    #print("Result: ",sub(a,b))
#elif choice==3:
    #a = int(input("Enter first number: "))
    #b = int(input("Enter first number: "))
    #print("Result: ",mul(a,b))
#elif choice==4:
    #a = int(input("Enter first number: "))
    #b = int(input("Enter first number: "))
    #print("Result: ",div(a,b))
#elif choice==5:
    #print("Quiting.......")


    if choice==1:
        print("Result: ",add(a,b))
    elif choice==2:
        print("Result: ",add(a,b))
    elif choice==3:
        print("Result: ",mul(a,b))
    elif choice==4:
        print("Result: ",div(a,b))
    elif choice==5:
        print("Quiting.....")
        break
    else:
        print("Invalid choice , try again!")






    