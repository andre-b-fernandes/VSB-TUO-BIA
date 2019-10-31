# The Michalewicz function has d! local minima, and it is multimodal. 
# The parameter m defines the steepness of they valleys and ridges; a larger m leads to a more difficult search. 
# The recommended value of m is m = 10.
import numpy as np
import math

# Make data.
X = np.arange(0, 4, 0.25)
Y = np.arange(0, 4, 0.25)
X_mesh, Y_mesh = np.meshgrid(X, Y)

d = 2

m = 10

sum_sq_term = np.sin(X_mesh)*np.power(np.sin(X_mesh*X_mesh/np.pi), 2*m) + np.sin(Y_mesh)*np.power(np.sin(d*Y_mesh*Y_mesh/np.pi), 2*m)

Z_mesh = - sum_sq_term

def Z(x,y):
    sum_sq_term = math.sin(x)*math.pow(math.sin(x*x/math.pi), 2*m) + math.sin(y)*math.pow(math.sin(d*y*y/math.pi), 2*m)
    z = - sum_sq_term
    return z

