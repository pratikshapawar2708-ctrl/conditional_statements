'''
program to check whether the password is valid or not using nested if 
'''

password = input("Enter your Password: ")

if len(password) >= 8:
    if password == "Python123":
        print("Password is valid.")
    else:
        print("Password is incorrect.")
else:
    print("Password must be at least 8 characters long.")