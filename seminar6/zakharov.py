# The Zakharov function has no local minima except the global one. It is shown here in its two-dimensional form. 
import numpy as np

# Make data.
X = np.arange(-10, 10, 0.25)
Y = np.arange(-10, 10, 0.25)
X_mesh, Y_mesh = np.meshgrid(X, Y)

d = 2

first_sum_sq_term = X_mesh*X_mesh +Y_mesh*Y_mesh
second_sum_sq_term = (0.5*X_mesh + 0.5*d*Y_mesh)*(0.5*X_mesh + 0.5*d*Y_mesh)
third_sum_sq_term = (0.5*X_mesh + 0.5*d*Y_mesh)*(0.5*X_mesh + 0.5*d*Y_mesh)*(0.5*X_mesh + 0.5*d*Y_mesh)*(0.5*X_mesh + 0.5*d*Y_mesh)

Z_mesh = first_sum_sq_term + second_sum_sq_term + third_sum_sq_term

def Z(x,y):
    first_sum_sq_term = x*x +y*y
    second_sum_sq_term = (0.5*x + 0.5*d*y)*(0.5*x + 0.5*d*y)
    third_sum_sq_term = (0.5*x + 0.5*d*y)*(0.5*x + 0.5*d*y)*(0.5*x + 0.5*d*y)*(0.5*x + 0.5*d*y)

    z = first_sum_sq_term + second_sum_sq_term + third_sum_sq_term
    return z