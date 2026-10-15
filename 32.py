'''
Program to check Whether a student is Eligible for an exam.
'''

attendance=int(input("Enter the Attendance of Student : "))
marks=int(input("Enter the Marks of Student : "))
if attendance>=75 and marks >=36 :
	print("The Student is Eligible for Exam...")
else:
	print("The Student is not Eligible for Exam...")