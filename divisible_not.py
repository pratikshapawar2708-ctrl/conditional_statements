'''
program is for number is divisible by 3 and 7 or not
'''
num=(int(input('Enter the number=')))
if num % 3 == 0:
        print(f'{num} is divisible by 3')
elif num % 7 ==0:
        print(f'{num} is divisible by 7')
else :
        print('The is not divisible by both')