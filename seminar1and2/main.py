import ackley
import griewank
import levy
import michalewicz
import rastrigin
import rosenbrock
import schwefel
import sphere
import zakharov
import blind_search_algorithm
import hill_climbing
import simulated_annealing

import sys, getopt

from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

function_name = getopt.getopt(sys.argv[1:],"")[1][0]
algorithm_name = getopt.getopt(sys.argv[1:],"")[1][1]

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

algorithm_mapping = {
    "blind_search" : blind_search_algorithm,
    "hill_climbing" : hill_climbing,
    "simulated_annealing" : simulated_annealing
}

try:
    function = function_mapping[function_name]
    algorithm = algorithm_mapping[algorithm_name]
    tup_min = algorithm.algorithm(function.X, function.Y, function.Z)
    print("Coordinates of x : " + str(tup_min[0]))
    print("Coordinates of y : " + str(tup_min[1]))
    print("Coordinates of z : " + str(tup_min[2]))

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Plot the surface.
    surf = ax.plot_surface(function.X_mesh, function.Y_mesh, function.Z, cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)

    ax.scatter(*tup_min, marker= 'D')

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)
    
    plt.show()
except KeyError:
    print("No function or algorithm with that name.")