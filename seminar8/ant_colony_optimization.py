import random
import numpy
import copy

class AntColonyOptimization:

    def __init__(self, visibility_matrix, number_of_ants, number_of_iterations = 100):
        self.original_visibility_matrix = visibility_matrix
        self.pheromone_matrix = self.generate_pheromone_matrix()
        self.n_ants = number_of_ants
        self.alpha = 1
        self.beta = 2
        self.evaporation_quoefficient = 0.5
        self.n_iter = number_of_iterations

    def generate_pheromone_matrix(self):
        return [ [1 for distance in distances ] for distances in self.original_visibility_matrix]

    def ant_colony_optimization(self):
        for _i in range(0, self.n_iter):
            ants = self.generate_ants()
            for ant in ants:
                self.calculate_route_for_ant(ant)
                self.calculate_pheromone_matrix(ant)
        return ants
        
    def generate_starting_cities(self):
        return random.sample(range(0, len(self.original_visibility_matrix)), self.n_ants)
    
    def generate_ants(self):
        starting_cities = self.generate_starting_cities()
        return [ [starting_cities[i]] for i in range(0, self.n_ants)]
       
    def calculate_pheromone_matrix(self, ant):
        distance = sum([ self.original_visibility_matrix[ant[i]][ant[i + 1]] for i in range(0, len(ant) - 1) ])
        for y in range(0, len(self.pheromone_matrix)):
            for x in range(0, len(self.pheromone_matrix[y])):
                self.pheromone_matrix[y][x] = (1 - self.evaporation_quoefficient)*self.pheromone_matrix[y][x] + 1/distance
    
    def calculate_route_for_ant(self, ant):
        number_of_cities = len(self.original_visibility_matrix) - 1
        vis_matrix = copy.deepcopy(self.original_visibility_matrix)
        for i in range(0, number_of_cities):
            ant.append(self.calculate_next_city(ant, vis_matrix))
    
    def calculate_next_city(self, ant, vis_matrix):
        city_index = ant[len(ant) - 1]
        for distances in vis_matrix:
            distances[city_index] = 0
        
        distances_cities = list(vis_matrix[city_index])
        pheromones_row = list(self.pheromone_matrix[city_index])

        probabilities = self.calculate_probabilities(distances_cities, pheromones_row)
        return self.calculate_probability_next_city(probabilities)

    def calculate_probabilities(self, distances_row, pheromones_row):
        values = list(map(lambda x,y: (x**self.beta)*(y**self.alpha), distances_row, pheromones_row))
        sum_values = sum(values)
        cum_probs = list(numpy.cumsum(list(map(lambda x: x/sum_values, values))))
        cum_probs.insert(0,0)
        return cum_probs
    
    def calculate_probability_next_city(self, cumulative_probs): 
        random_number = random.uniform(0,1)
        for i in range(0, len(cumulative_probs) - 1):
            if random_number >= cumulative_probs[i] and random_number < cumulative_probs[i + 1]:
                return i
        raise ValueError("There is no interval in the cumulative probabilities for the random generated number of: " + random_number)
        