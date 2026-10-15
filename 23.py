'''
program to Calculate Electricity Bill based on units consumed
'''

units = int(input("Enter units consumed: "))
if units <= 100:
    bill = units * 5
else :
	    bill = (100 * 5) + (units - 100) * 7
print("Electricity Bill =", bill)