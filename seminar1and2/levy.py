import numpy as np

# Make data.
X = np.arange(-10, 10, 0.25)
Y = np.arange(-10, 10, 0.25)
X, Y = np.meshgrid(X, Y)

d = 2
wx = 1 + ( X - 1)/4
wy = 1 + ( Y - 1)/4

sin_term = np.sin(np.pi * X)*np.sin(np.pi * X)
sum_seq_term = (wx-1)*(wx-1)*(1 + 10*np.sin(np.pi*wx + 1)*np.sin(np.pi*wx + 1))*(1 + 10*np.sin(np.pi*wx + 1)*np.sin(np.pi*wx + 1)) + (wy - 1)*(wy - 1)*(1 + np.sin(2*np.pi*wy)*np.sin(2*np.pi*wy))

Z = sin_term + sum_seq_term