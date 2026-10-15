'''
program for print the day name based on day number (1to7).
'''
day=(int(input('Enter the day [1-7]=')))
if day == 1:
    print('Monday')
elif day ==2:
    print('tuesday')
elif day == 3:
    print('Wednesday')
elif day == 4:
    print('thursday')
elif day == 5:
    print('friday')
elif day == 6:
    print('saturday')
elif day == 7:
    print('sunday')
else:
    print('Invalid input ! please enter the value between 1 to 7')