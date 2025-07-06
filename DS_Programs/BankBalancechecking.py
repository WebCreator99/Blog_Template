def menu():
    print("-----Banking System-----")
    print("1. Check Balnce")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Quit")

balance = 0

while True:
    menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Balance : ",balance)
    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        balance += amount
    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))
        balance -= amount

        
    elif choice == 4:
        print("Thank you for using our banking system")
        break
