# The Griewank function has many widespread local minima, which are regularly distributed. 
import numpy as np
import math

# Make data.
X = np.arange(-32, 32, 0.25)
Y = np.arange(-32, 32, 0.25)
X_mesh, Y_mesh = np.meshgrid(X, Y)

sum_sq_term = (X_mesh*X_mesh + Y_mesh*Y_mesh)/4000
cos_term = np.cos(X_mesh) * np.cos(Y_mesh)/np.sqrt(2)

Z_mesh = sum_sq_term + cos_term + 1

def Z(x,y):
    sum_sq_term = (x*x + y*y)/4000
    cos_term = math.cos(x) * math.cos(y)/math.sqrt(2)
    z = sum_sq_term + cos_term + 1
    return z
