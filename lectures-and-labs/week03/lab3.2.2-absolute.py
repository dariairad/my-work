# Lab 3.2.2
# Program that takes in number and gives its absolute value 
# (Input casted to a float based on output example included in the lab description)
# Author: Daria Sep

number = float (input ('Enter a number: '))
# abs() is a built in function
absoluteValue = abs (number)

print ('Absolute value of {} is {}' .format (number, absoluteValue))