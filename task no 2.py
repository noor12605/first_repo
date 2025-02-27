Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num=int(input("Enter your number:"))
Enter your number:-45
>>> if num > 0:
	print("number is positive")
elif num < 0:
	print("number is negative")
else:
	print("number is zero")

	
number is negative
>>> #no 2
>>> year=int(input("enter a year"))
enter a year 2025
>>> if year%4==0:
	print("this is a leap year")
else:
	print("this is not leap year")

	
this is not leap year
>>> #no 3
>>> num_1=float(input("enter a first number:"))
enter a first number:56
>>> num_2=float(input("enter a second number:"))
enter a second number:12
>>> operator=input("enter an operator from +,-,*,/")
enter an operator from +,-,*,/ "*"
>>> if operator == "+":
	results=num_1+num_2
	print("the result is",results)
elif operator == "-":
	results=num_1-num_2
	print("the result is",results)
elif operator == "*":
	results=num_1*num_2
	print("the result is",results)
elif operator == "/":
	results=num_1/num_2
	print("the result is",results)
else:
	print("error! use correct operator")

	
error! use correct operator
>>> 