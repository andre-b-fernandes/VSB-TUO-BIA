import ackley
import griewank
import levy
import michalewicz
import rastrigin
import rosenbrock
import schwefel
import sphere
import zakharov

import sys, getopt

from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

from firefly_algorithm import FireflyAlgorithm


function_name = getopt.getopt(sys.argv[1:],"")[1][0]
iterations = int(getopt.getopt(sys.argv[1:],"")[1][1])
pop_size = int(getopt.getopt(sys.argv[1:],"")[1][2])

function_mapping = {
    "ackley": ackley,
    "griewank": griewank,
    "levy": levy,
    "michalewicz": michalewicz,
    "rastrigin": rastrigin,
    "rosenbrock": rosenbrock,
    "schwefel": schwefel,
    "sphere": sphere,
    "zakharov": zakharov
}


try:
    function = function_mapping[function_name]
    firefly_algorithm = FireflyAlgorithm(function.X, function.Y, function.Z)
    tup_min = firefly_algorithm.process(iterations, pop_size)

    print("Coordinates of x : " + str(tup_min[0]))
    print("Coordinates of y : " + str(tup_min[1]))
    print("Coordinates of z : " + str(tup_min[2]))

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    # Plot the surface.
    surf = ax.plot_surface(function.X_mesh, function.Y_mesh, function.Z_mesh, cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)

    ax.scatter(*tup_min, marker= 'D')

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)
    
    plt.show()
except KeyError:
    print("No function or algorithm with that name.")    