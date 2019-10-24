# The Schwefel function is complex, with many local minima. The plot shows the two-dimensional form of the function.
import numpy as np
import math

# Make data.
X = np.arange(-500, 500, 0.25)
Y = np.arange(-500, 500, 0.25)
X_mesh, Y_mesh = np.meshgrid(X, Y)

d = 2

sum_sq_term = X_mesh*np.sin(np.sqrt(np.absolute(X_mesh))) + Y_mesh*np.sin(np.sqrt(np.absolute(Y_mesh)))

Z_mesh = 418.9829*d + sum_sq_term

def Z(x,y):
    sum_sq_term = x*math.sin(math.sqrt(abs(x))) + y*math.sin(math.sqrt(abs(y)))
    z = 418.9829*d + sum_sq_term
    return z