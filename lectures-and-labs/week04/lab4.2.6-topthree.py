# Lab 4.2.6

# Program that generates 10 random numbers (0-100), prints them out then prints out the top three. 

# Author: Daria Sep

# Ref provided: https://stackoverflow.com/questions/32296887/how-to-find-the-1st-2nd-3rd-highest-values-in-a-list-in-python

import random 

howMany = 10
topHowMany = 3
rangeFrom = 0
rangeTo = 100

numbers = [] 

for i in range(0,10):
    numbers.append (random.randint (rangeFrom, rangeTo))
print ('{} random numbers\t {}' .format (howMany, numbers))

topOnes = numbers.copy ()
topOnes.sort (reverse = True)
print ('The top {} are \t\t {}' .format (topHowMany, topOnes [0:topHowMany]))