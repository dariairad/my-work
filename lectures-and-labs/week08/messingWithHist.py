# Lecture 8.2 - Histogram

import numpy as np
import matplotlib.pyplot as plot

np.random.seed(1) # random sample stays the same, handy for debugging
normData = np.random.normal (size=10) # it won't be normalized until saize is big enough eg. 10000

plot.hist (normData)
plot.show ()