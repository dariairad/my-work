# Lab 8.6

# Write a program that plots a histogram of the salaries (from Question 1)

import numpy as np
import matplotlib.pyplot as plot

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

np.random.seed (1)
salaries = np.random.randint (minSalary, maxSalary, numberOfEntries)

plot.hist (salaries)
plot.show ()