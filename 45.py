'''
Program to print menu based  food Selection using Matchcase
'''
print("1. Pizza")
print("2. Burger")
print("3. Sandwich")
choice = int(input("Enter your choice (1, 2, or 3): "))
match choice:
    case 1:
        print("You selected Pizza")
    case 2:
        print("You selected Burger")
    case 3:
        print("You selected Sandwich")
    case _:
        print("Invalid choice")