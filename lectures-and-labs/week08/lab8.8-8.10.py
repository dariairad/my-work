# Lab 8.8, 8.9 & 8.10

# Add a line to this plot (lab8.7.py) that shows y= x2 in a different colour.
# Add a legend, title and axis labels to this plot.
# Save this to a file called “prettier-plot.py”

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

plot.scatter (ages, salaries, label = 'salaries')

xpoints = np.array (range(1,101))
ypoints = xpoints * xpoints 

plot.plot (xpoints, ypoints, color = 'r', label = 'x squared')

plot.title ('Random Plot')
plot.xlabel ('Salaries')
plot.ylabel ('Age')
plot.legend ()

plot.savefig ('prettier-plot.png')
