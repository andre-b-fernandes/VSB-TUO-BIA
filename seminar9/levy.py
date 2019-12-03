import numpy as np
import math

# Make data.
X = np.arange(-10, 10, 0.25)
Y = np.arange(-10, 10, 0.25)
X_mesh, Y_mesh = np.meshgrid(X, Y)

d = 2
wx = 1 + ( X_mesh - 1)/4
wy = 1 + ( Y_mesh - 1)/4

sin_term = np.sin(np.pi * X)*np.sin(np.pi * X)
sum_seq_term = (wx-1)*(wx-1)*(1 + 10*np.sin(np.pi*wx + 1)*np.sin(np.pi*wx + 1))*(1 + 10*np.sin(np.pi*wx + 1)*np.sin(np.pi*wx + 1)) + (wy - 1)*(wy - 1)*(1 + np.sin(2*np.pi*wy)*np.sin(2*np.pi*wy))

Z_mesh = sin_term + sum_seq_term

def Z(x,y):
    wx = 1 + ( x - 1)/4
    wy = 1 + ( y - 1)/4
    sin_term = math.sin(math.pi * x)*math.sin(math.pi * x)
    sum_seq_term = (wx-1)*(wx-1)*(1 + 10*math.sin(math.pi*wx + 1)*math.sin(math.pi*wx + 1))*(1 + 10*math.sin(math.pi*wx + 1)*math.sin(math.pi*wx + 1)) + (wy - 1)*(wy - 1)*(1 + math.sin(2*math.pi*wy)*math.sin(2*math.pi*wy))
    z = sin_term + sum_seq_term
    return z