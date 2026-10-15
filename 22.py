'''
to check the salary bonus based on year of services
'''

year=int(input("Enter years of Services : "))
salary=int(input("Enter the Salary : "))
if year >=2 :
    bonus=salary*5/100
    print("the Bonus is : ",bonus)
elif year>=5:
	bonus=salary*10/100
	print("the Bonus is : ",bonus)
else :
    	print("No bonus for youu....")