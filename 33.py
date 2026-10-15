'''
Program to check whether a person can apply for loan or not
'''
age= int(input("Enter your age= "))
salary = int(input("Enter your salary= "))

if age >= 21 and age < 60:

	if salary >= 25000 and salary < 40000:
        	print("You can apply for a loan up to Rs. 2,00,000")

	elif salary >= 40000 and salary < 60000:
		print("You can apply for a loan up to Rs. 5,00,000")

	elif salary >= 60000:
		print("You can apply for a loan up to Rs. 10,00,000")

	else:
		print("Your salary is too low for a loan")

else:
    print("You are not eligible for a loan")