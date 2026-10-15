'''
program to find the smallest of three numbers.
'''
num1=(int(input('Enter the number=')))
num2=(int(input('Enter the number=')))
num3=(int(input('Enter the number=')))
if num1<=num2 and num1<=num3:
        print('The num1 is smallest')
elif num2<=num1 and num2<=num3:
        print('The num2 is smallest')
elif num3<=num1 and num3<=num2:
        print('The num3 is smallest')
else :
        print('Invalid input ! Enter the correct number')