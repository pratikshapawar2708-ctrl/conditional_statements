'''
program to check ticket price based on age.
'''
age =(int(input('Enter the age=')))
if age<=7:
    print('Ticket price:free')
elif age<=18:
    print('Ticket price:60')
elif age<=70:
    print('Ticket price:100')
else:
    print('Ticket price:80')
