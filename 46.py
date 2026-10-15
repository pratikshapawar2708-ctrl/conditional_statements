'''
program to print grade description using Match Case
'''
grade = input("Enter your grade (O,A+,A,B,F): ")

match grade:
    case "O":
        print("Outstanding")
    case "A+":
        print("Very Good")
    case "A":
        print("Good")
    case "B":
        print("Needs Improvement")
    case "F":
        print("Fail")
    case _:
        print("Invalid grade")