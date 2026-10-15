'''
program to build a simple ATM menu using Match case
'''
balance = int(input("Enter your Current Balance : "))
print("1. Check balance")
print("2. Deposit money")
print("3. Withdraw money")
choice = int(input("Choose an option (1–3): "))
match choice:
    case 1:
        print("Your balance is:", balance)
    case 2:
        amount = int(input("Enter deposit amount: "))
        balance = balance + amount
        print("New balance:", balance)
    case 3:
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance = balance - amount
            print("New balance:", balance)
        else:
            print("Insufficient balance")
    case _:
        print("Invalid choice")