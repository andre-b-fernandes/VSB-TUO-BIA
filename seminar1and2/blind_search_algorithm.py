import random
import sys

def algorithm(x_points, y_points, z_points):
    size = min(len(x_points), len(y_points))
    x_max = len(x_points) - 1
    y_max = len(y_points) - 1
    pop = generate_population(size, x_max, y_max)
    i = 0
    tup_min = (None, None)
    while(i < 3000):
        tup_min = evaluation_function(pop, z_points)
        pop = generate_population(size - 1, x_max, y_max)
        pop.append(tup_min)
        i += 1

    z_min = z_points[tup_min[1]][tup_min[0]]
    x_min = x_points[tup_min[0]]
    y_min = y_points[tup_min[1]]
    return (x_min, y_min, z_min)


def generate_population(size, tupx_max, tupy_max):
    #initial pop
    pop = []
    i = 0
    while i < size:
        pop.append(( random.randint(0,tupx_max) , random.randint(0,tupy_max)  )) # (index x, index y)
        i += 1
    return pop

def evaluation_function(pop, z_points):
    minimum = sys.maxsize
    index = None
    counter = 0
    while counter < len(pop): # selection -> elitism
        x_index = pop[counter][0]
        y_index = pop[counter][1]
        z_val = z_points[y_index][x_index]
        if z_val < minimum:
            minimum = z_val
            index = counter
        counter += 1
    tup_min = pop[index]
    return tup_min
