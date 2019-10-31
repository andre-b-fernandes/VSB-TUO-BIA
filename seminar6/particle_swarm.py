import numpy
import random
import time

from sys import maxsize
from particle import Particle
from math import sqrt


class ParticleSwarm:
    
    def __init__(self, x , y , z, pop_size = 100, num_iterations = 1000):
        self.x_list = x
        self.y_list = y
        self.z_function = z
        self.population_size = pop_size
        self.iterations = num_iterations

    
    def particle_swarm_algorithm(self):
        pop = self.generate_initial_population()
        for i in range(0, self.iterations):
            self.global_best.print_self()
            self.next_population(pop)
            
        self.global_best.print_self()
        return (self.global_best.coords[0], self.global_best.coords[1], self.global_best.fitness)
    
    def generate_initial_population(self):
        pop = []
        
        copy_x = numpy.array(self.x_list, copy=True)
        copy_y = numpy.array(self.y_list, copy=True)

        for i in range(0, self.population_size):
            element_x = random.choice(copy_x)
            element_y = random.choice(copy_y)
            particle = Particle(element_x, element_y)
            particle.set_particle_fitness(self.z_function)
            pop.append(particle)

        self.global_best = min(pop)
        self.global_best.set_velocity(0,0)

        for particle in pop:
            velocity = (self.global_best.coords[0] - particle.coords[0], self.global_best.coords[1] - particle.coords[1])
            norm_velocity = sqrt(velocity[0]*velocity[0] + velocity[1]*velocity[1])
            if norm_velocity == 0:
                norm_velocity = 1
            velocity_normalized = (velocity[0]/norm_velocity, velocity[1]/norm_velocity)
            particle.set_velocity(velocity_normalized[0], velocity_normalized[1])

        return pop
    
    def next_population(self, population):
        for particle in population:
            particle.set_particle_fitness(self.z_function)
            self.calculate_next_velocity(particle)
            particle.update_coords()
            particle.set_particle_best(self.z_function)
        
        self.global_best = min(population)
        self.global_best.set_velocity(0,0)


    def calculate_next_velocity(self, individual):
        learning_factor_1, learning_factor_2 = 2,2
        next_velocity_x = individual.velocity_coords[0] + learning_factor_1*random.uniform(0,1)*( individual.best_coords[0] - individual.coords[0] ) + learning_factor_2*random.uniform(0,1)*(self.global_best.coords[0] - individual.coords[0])
        next_velocity_y = individual.velocity_coords[1] + learning_factor_1*random.uniform(0,1)*( individual.best_coords[1] - individual.coords[1] ) + learning_factor_2*random.uniform(0,1)*(self.global_best.coords[1] - individual.coords[1])
        norm_next_velocity = sqrt(next_velocity_x * next_velocity_x + next_velocity_y * next_velocity_y)
        if norm_next_velocity == 0:
            norm_next_velocity = 1
        individual.set_velocity(next_velocity_x/norm_next_velocity, next_velocity_y/norm_next_velocity)
        
        

    
    

    
