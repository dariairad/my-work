# Lab 8.3
# Modify the program, to make another array of numbers that has the salaries plus 5000 
# (numpy is great for matrix operations)

import numpy as np

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed (1) ### 
salaries = np.random.randint (minSalary, maxSalary, numberOfEntries)
salariesPlus = salaries + 5000

print (salariesPlus)