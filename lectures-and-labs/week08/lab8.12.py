# Lab 8.12

# Make some counties appear more than others. Make a pie chart of the counties.

import numpy as np
import  matplotlib.pyplot as plot

possibleCounties = ['Dublin', 'Mayo', 'Kilkenny', 'Galway', 'Wicklow']

counties = np.random.choice (
    possibleCounties,
    p = [0.1, 0.3, 0.2, 0.12, 0.28],
    size = 100
) 

unique, counts = np.unique (counties, return_counts = True)

plot.bar (counts, unique)

plot.show()