import json, getopt, sys, math
from ant_colony_optimization import AntColonyOptimization


def calculate_distance_matrix(cities):
    return [ [math.sqrt( ((city['x'] - another_city['x']) ** 2) + ((city['y'] - another_city['y']) ** 2) ) for another_city in cities] for city in cities ]

def calculate_visibility_matrix(distance_matrix):
    vis_matrix = [ [ 1/distance if distance != 0 else 0 for distance in distances ] for distances in distance_matrix]
    return vis_matrix

def visualize_solution(trajectory, cities, distance_matrix):
    for element in trajectory:
        print( cities[element]["name"] + "->", end="")
    distance = calculate_distance(trajectory, distance_matrix)
    print("Total distance: " + str(distance))

def calculate_distance(trajectory, distance_matrix):
    return sum([ distance_matrix[trajectory[i]][trajectory[i + 1]] for i in range(0, len(trajectory) - 1) ])

n_ants = int(getopt.getopt(sys.argv[1:],"")[1][0])
n_iter = int(getopt.getopt(sys.argv[1:],"")[1][1])

with open('cities.json') as cities_json_file:
    cities_json = json.load(cities_json_file)
    distance_matrix = calculate_distance_matrix(cities_json['cities'])
    visibility_matrix = calculate_visibility_matrix(distance_matrix)
    ant_colony_wrapper = AntColonyOptimization(visibility_matrix, n_ants, n_iter)
    trajectories = ant_colony_wrapper.ant_colony_optimization()
    min_traj = min(trajectories, key= lambda trajectory: calculate_distance(trajectory,distance_matrix))
    visualize_solution(min_traj, cities_json['cities'], distance_matrix)