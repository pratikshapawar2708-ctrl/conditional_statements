'''
program is check three number of greatest
'''
num1=(int(input('Enter the munber=')))
num2=(int(input('Enter the number=')))
num3=(int(input('Enter the number=')))
if num1>=num2 and num1>=num3:
    print('The num1 is greatest')
elif num2>=num1 and num2>=num3:
    print('The num2 is greatest')
else :
    print('The num3 is greatest')