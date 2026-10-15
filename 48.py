'''
program to print language choice by using match case
''' 
print("1. Python")
print("2. Java")
print("3. C++")

choice = int(input("Choose a language : "))

match choice:
    case 1:
        print("You choose Python")
    case 2:
        print("You choose Java")
    case 3:
        print("You choose C++")
    case _:
        print("Invalid choice")