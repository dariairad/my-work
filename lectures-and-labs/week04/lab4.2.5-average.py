# Lab 4.2.1

# Program that keeps reading numbers until the user enters a 0. 
# The program appends each of them into a list.
# The program then prints out each of the numbers entered and the average of them. 

# Author: Daria Sep

import numbers


numbers = []

number = int (input ('Enter a number (0 to quit): '))

while number != 0:
    numbers.append(number)

    # read the next number to check if 0
    number = int (input ('Enter another number (0 to quit): '))

for value in numbers:
    print (value) 

average = float (sum (numbers)) / len(numbers)
print ('The average is {}' .format (average))
