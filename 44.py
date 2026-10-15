'''
Program to check Traffic Signal actions using Matchcase
'''
print("1. Red")
print("2. Yellow")
print("3. Green")
signal =int( input("Enter traffic signal color  :  "))
match signal:
    case 1 :
        print("Stop")
    case 2 :
        print("Get ready")
    case 3 :
        print("Go")
    case _:
        print("Invalid signal color")