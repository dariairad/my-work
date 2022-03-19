# Lecture 8.1 - Numpy

import numpy as np

list = [1,2,3,4]
number = np.array([1,2,3,4])

number = number + 1 # adds one to each value 

print (list)
print (number)

number = number * 3 # myltiply each value by 3
print (number)

number = number * np.array([1,2,3,4]) # multiplies original values by valued in respective possitions
print (number)#

random = np.random.randint(100, 200, 5)  # generates random numbers
print (random)
