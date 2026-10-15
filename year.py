'''
program year leap or not
'''
year=(int(input('Enter the year:')))
if year % 400==0:
    print(f'This{year}is leap year')
#The example 2000 its divided by 400 return 0 it's leap year
elif year % 100==0:
    print(f'This{year}is not leap year')  
 #1900 is not a leap year because it is divisible by 100 but not by 400
elif year % 4==0:
    print(f'The{year}is leap year')
#Divide 2024 by 4 its 2024 divisible 4 = 506 remainder 0
else:
    print(f'The{year}is not leap year')
