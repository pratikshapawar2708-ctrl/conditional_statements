'''
program to Check blood donation eligibility based on age and weight
'''

age = int(input("Enter your age= "))
weight=int(input("Enter your weight= "))

if age >=18 and weight >=50:
	print("You are eligible for blood donation")
else:
	print("You are not eligible for blood donation")