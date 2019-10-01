'''
-------------------------------------------------------------------------------
Name:		practice1.py
Purpose:	fahrentheit to celsius converter

Author:	Lui.A

Created:	date in 01/10/2019
------------------------------------------------------------------------------
'''


# get fahrenheit from user
fahrenheit = float(input("Enter the fahrenheit: "))

# compute celcius from fahrenheit
celsius = (5/9) * (fahrenheit - 32)

# output celcius
print("the temperature in celsius is", celsius)
