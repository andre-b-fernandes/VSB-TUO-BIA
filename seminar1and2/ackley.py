
# The Ackley function is widely used for testing optimization algorithms.
# In its two-dimensional form, as shown in the plot above, it is characterized by a nearly flat outer region, and a large hole at the centre. The function poses a risk for optimization algorithms, particularly hillclimbing algorithms, to be trapped in one of its many local minima.
# Recommended variable values are: a = 20, b = 0.2 and c = 2π.
import numpy as np

# Make data.
X = np.arange(-32, 32, 0.25)
Y = np.arange(-32, 32, 0.25)
X_mesh, Y_mesh = np.meshgrid(X, Y)

a = 20
b = 0.2
c = 2 * np.pi

sum_sq_term = -a * np.exp(-b * np.sqrt(X_mesh*X_mesh + Y_mesh*Y_mesh) / 2)
cos_term = -np.exp((np.cos(c*X_mesh) + np.cos(c*Y_mesh)) / 2)
Z = a + np.exp(1) + sum_sq_term + cos_term