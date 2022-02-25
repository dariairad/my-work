# Lab 4.1.3 Extra
# Program from Lab 4.1.2 (lab4.1.2-grade.py) modified to round percentage to the nearest integer eg. 69.5 rounds up to 70

# Author: Daria Sep

import math


percentage = float (input ('Enter the percentage: '))
# using round() is not accurate. some x.5 numbers are rounded up some down
# using math.floor () function instead > it rounds a number down to the nearest integer
# on it's own would not work accurately, but we can overcome it by adding 0.5 to an input percentage
# If the digit in the first decimal place of the shifted value is less than five, then adding 0.5 won’t change the integer part of the shifted value, so the floor is equal to the integer part.
# If the first digit after the decimal place is greater than or equal to 5, then adding 0.5 will increase the integer part of the shifted value by 1, so the floor is equal to this larger integer.
# ref: https://realpython.com/python-rounding/#:~:text=To%20implement%20the%20%E2%80%9Crounding%20up,equal%20to%20a%20given%20number.
percentageRounded = math.floor(percentage + 0.5)


if percentageRounded < 0 or percentage > 100:
    print ('Please enter a number between 0 and 100')
elif percentageRounded < 40:
    print ('Fail')
elif percentageRounded < 50:
    print ('Pass')
elif percentageRounded < 60:
    print ('Merit 1')
elif percentageRounded < 70:
    print ('Merit 2')
else:
    print ('Distinction')
