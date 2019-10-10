# The Rosenbrock function, also referred to as the Valley or Banana function, is a popular test problem for gradient-based optimization algorithms.
# The function is unimodal, and the global minimum lies in a narrow, parabolic valley. 
# However, even though this valley is easy to find, convergence to the minimum is difficult (Picheny et al., 2012). 
import numpy as np

# Make data.
X = np.arange(-10, 10, 0.25)
Y = np.arange(-10, 10, 0.25)
X_mesh, Y_mesh = np.meshgrid(X, Y)

d = 2


sum_sq_term = 100*(Y_mesh - X_mesh*X_mesh)*(Y_mesh - X_mesh*X_mesh) + (X_mesh-1)*(X_mesh-1)

Z = sum_sq_term