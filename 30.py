'''
program to check whether the number is single ,double or three digit.
'''
num=int(input("Enter a  Number : "))
if  num //10==0 :	
	print("Number is Single digit .")
elif num//100==0 :
	print("Number is Double digit .")
elif num//1000==0 :
	print("Number is Three digit .")
else : 
	print("Number is more than Three digit no .")