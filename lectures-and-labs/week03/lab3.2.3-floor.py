# Lab 3.2.3

# Program that takes in a float and outputs an int rounded down (using math module math.floor())
# math.floor() returns the floor of x, the largest integer less than or equal to x. 
# Ref: https://docs.python.org/3/library/math.html#math.floor)

# Author: Daria Sep

import math

numberToFloor = float (input ('Enter a float number: '))
flooredNumber = math.floor (numberToFloor)

print ('{} floored is {}' .format (numberToFloor, flooredNumber))