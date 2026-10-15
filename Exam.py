'''
Program to check the rasult
'''
marks=(int(input('Enter the marks=')))
if marks>=75:
    print('Result:Distinction')
elif marks>=60:
    print('Result:First class')
elif marks>=40:
    print('Result:pass')
else:
    print('Result:fail')