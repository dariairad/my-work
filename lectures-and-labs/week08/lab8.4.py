# Lab 8.4
# Modify the program so that it increases all the salaries by 5% (store in another array).


import numpy as np

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed (1) ### 
salaries = np.random.randint (minSalary, maxSalary, numberOfEntries)
salariesMult = salaries * 1.5

print (salariesMult)

newSalaries = salariesMult.astype (int) # converting to an int array, it does the floor
print (newSalaries)