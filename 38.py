'''
Program to check whether the student passed  all subject or not
'''
maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

if maths >= 35 and science >= 35 and english >= 35:
    print("The student passed all subjects.")
else:
    print("The student did not pass all subjects.")
