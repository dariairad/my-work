# Lab 3.1.4 v2
# Program that prints out a random number from a range selected by the user
# Author: Daria Sep


import random

print ("Fancy a random number? \nChoose your range: ")

x = int (input ('From: '))
y = int (input ('To : '))

number = random.randint (x, y)
print ('Here is your random number: {}' .format (number))