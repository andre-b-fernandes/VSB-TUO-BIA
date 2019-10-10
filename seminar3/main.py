from city import City
from genetic_algorithm import GeneticAlgorithm

import json, getopt, sys

pop_size = int(getopt.getopt(sys.argv[1:],"")[1][0])
n_iter = int(getopt.getopt(sys.argv[1:],"")[1][1])


with open('cities.json') as json_file:
    cities_json = json.load(json_file)
    cities = []
    for c in cities_json['cities']:
        cities.append(City(c['name'], int(c['x']), int(c['y'])))

    generic_algorithm = GeneticAlgorithm(cities)
    solution = generic_algorithm.algorithm(pop_size, n_iter)
    solution.print_chromossomes()
    