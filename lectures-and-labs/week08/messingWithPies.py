# Lecture 8.2 - Plotting - Pie charts

import numpy as np
import matplotlib.pyplot as plot

fruit = np.array (['Apple', 'Orange', 'Banana'])
numbers = np.array ([23, 77, 300])

plot.pie (numbers, labels = fruit)
plot.legend ()
plot.show ()