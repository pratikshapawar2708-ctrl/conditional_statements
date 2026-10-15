'''
program to check whether a year is leap year or centuary year
'''
year=int(input("Enter the Year  : "))
if year%4==0:
	print("The Year is Leap Year...")
	if year%100==0:
		print("The Year is Centuary Year...")
	else :
		print("The Year is Not Centuary Year...")
else :
	print("The Year is Not Leap Year...")

