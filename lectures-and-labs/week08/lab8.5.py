# Lab 8.5
# Write a program that plots the function y = x2.

import matplotlib.pyplot as plot
import numpy as np

xpoints = np.array (range(1,101))
ypoints = xpoints * xpoints 

plot.plot (xpoints, ypoints)
plot.show ()
