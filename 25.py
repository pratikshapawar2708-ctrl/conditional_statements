'''
program to check whteher the Trianlge is equilateral,Isosceles,or Scalene
'''
a=float(input("Enter First Side : "))
b=float(input("Enter Second Side : "))
c=float(input("Enter Third Side : ")) 
if a == b == c:
        print("This is an Equilateral Triangle.")
    elif a == b or a == c or b == c:
          print("This is an Isosceles Triangle.")
    else:
        return "Scalene"