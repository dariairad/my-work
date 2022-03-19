# Lab 8.11

# Write program that has a list of counties, make it a long list (pick from five counties). 
# (Demonstrate making a pie plot of the unique occurences of values in an array .)

import numpy as np
import  matplotlib.pyplot as plot

# array of occurancies
possibleCounties = ['Dublin', 'Mayo', 'Kilkenny', 'Galway', 'Wicklow']

# pick 100 randomly from possible counties with frequency 
counties = np.random.choice (
    possibleCounties,
    p = [0.1, 0.3, 0.2, 0.12, 0.28],
    size = 100
) 

# right now we need the number of occurences of each county
# this returns a tuple of the unique values and how many times they appear
unique, counts = np.unique (counties, return_counts = True)

# we can now put this into a pie plot
plot.pie (counts, labels = unique)

plot.show()