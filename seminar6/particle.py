from sys import maxsize

class Particle:
    
    def __init__(self, x, y):
        self.coords = (x,y)
        self.best_coords = (x, y)
        
    def set_particle_fitness(self, z_function):
        self.fitness = z_function(self.coords[0], self.coords[1])

    def set_particle_best(self, z_function):
        pbest = z_function(self.coords[0], self.coords[1])
        if pbest <= self.fitness:
            self.best_coords = self.coords

    def set_velocity(self, vx, vy):
        self.velocity_coords = (vx, vy)

    def update_coords(self):
        self.coords = (self.coords[0] + self.velocity_coords[0], self.coords[1] + self.velocity_coords[1])
    
    def print_self(self):
        print("\t------------------------------\r\n")
        print("\tFitness: " + str(self.fitness))
        print("\tCurrent spacial coordinates\n")
        print("\tX_coords: " + str(self.coords[0])+ "\tY_coords: " + str(self.coords[1]))
        print("\tBest spacial coordinates\n")
        print("\tX_coords: " + str(self.best_coords[0])+ "\tY_coords: " + str(self.best_coords[1]))
        print("\tCurrent Velocity coordinates\n")
        print("\tX_coords: " + str(self.velocity_coords[0])+ "\tY_coords: " + str(self.velocity_coords[1]))

    def __eq__(self, other_particle):
        return self.fitness == other_particle.fitness

    def __lt__(self, other_particle):
        return self.fitness < other_particle.fitness

    def __gt__(self, other_particle):
        return self.fitness > other_particle.fitness