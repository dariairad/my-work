# Lab 3.2.1
# Program that takes in a float and outpts an in (rounded up or down)
# Author: Daria Sep

# Converting input to a float so the round() function can be used with the input
numberToRound = float (input ("Enter a float number: "))
# round () is a built in function
roundedNumber = round (numberToRound)

# Using formatting to be able to print int/float with a message
print ('{} rounded is {}' .format (numberToRound, roundedNumber))