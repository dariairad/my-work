# Lab 8.7

# Write a program that makes a list called ages that has, the same number random values as salaries, 
# (range:21 to 65) . Make scatter plot of this data

import numpy as np
import matplotlib.pyplot as plot

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100
lowAge = 21
highAge = 65

np.random.seed (1)
salaries = np.random.randint (minSalary, maxSalary, numberOfEntries)
ages = np.random.randint (lowAge, highAge, numberOfEntries)
# ages = np.random.randint(low=21, high = 65, size = numberOfEntries) 

plot.scatter (ages, salaries)
plot.show ()