# The Sphere function has d local minima except for the global one. It is continuous, convex and unimodal.
import numpy as np

# Make data.
X = np.arange(-10, 10, 0.25)
Y = np.arange(-10, 10, 0.25)
X_mesh, Y_mesh = np.meshgrid(X, Y)

d = 2

sum_sq_term = X_mesh*X_mesh + Y_mesh*Y_mesh

Z_mesh = sum_sq_term

def Z(x,y):
    sum_sq_term = x*x + y*y
    z = sum_sq_term
    return z