'''
program to check user role(admin , user, guest) using Match case
'''
print("1. Admin")
print("2. User")
print("3. Guest")

role = int(input("Enter your choice: "))

match role:
    case 1:
        print("Admin role")
    case 2:
        print("User role")
    case 3:
        print("Guest role")
    case _:
        print("Invalid choice")