'''
Program to print result status using match case
'''
print("1. Pass")
print("2. Fail")
print("3. Absent")

choice = int(input("Enter result status : "))

match choice:
    case 1:
        print("Result: Pass")
    case 2:
        print("Result: Fail")
    case 3:
        print("Result: Absent")
    case _:
        print("Invalid choice")