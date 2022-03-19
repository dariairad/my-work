# Lab 8.1 
# Write a program that makes a list, called salaries, that has (say 10) random numbers (20000 – 80000)

import numpy as np

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

salaries = np.random.randint (minSalary, maxSalary, numberOfEntries)

print (salaries)