'''
program tto Check Whether the  number is Positive and Even using nested if
'''
num=int(input("Enter a Number : "))
if num >0 :
	print("The Given Number is Positive Number.")
	if num%2==0 :
		print("The Given Number is an Even Number.")
	else:
		print("The Given Number is Not an Even Number.")
else:
	print("The Number is Negative Number.")