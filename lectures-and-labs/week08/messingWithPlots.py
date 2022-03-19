# Lecture 8.2 - Plotting

# Plot and scatter 

import numpy as np
import matplotlib.pyplot as plot

xpoints = np.array (range (1, 101))
ypoints = xpoints * xpoints

plot.plot (xpoints, ypoints, label = 'xsquared')
plot.plot (xpoints, xpoints, label = 'straight', color = 'green')
plot.legend ()

randomPoints = np.random.randint (1, 1000, 100)
plot.scatter (xpoints, randomPoints, label = 'random', color = 'orange')

plot.show ()
# plot.savefig ('lecture8.2.png')