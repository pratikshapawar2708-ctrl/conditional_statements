'''
program to check exam results.
'''
mark=int(input("Enter the marks of student : "))
if  mark >85 :
	print("Distinction....")
elif mark > 65 :
	print("First Class....")
elif  mark > 36 :
        print("Pass....")
else :
	print("Fail.")