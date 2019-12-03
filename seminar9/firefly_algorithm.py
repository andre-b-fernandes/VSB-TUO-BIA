import random, math

class FireflyAlgorithm:
    
    def __init__(self, x, y, z):
        self.x_coords = x
        self.y_coords = y
        self.z_function = z
        self.light_absortion_coefficient = 1
        self.attractiveness_null_distance = 1
        self.alpha = 0.25
        self.x_min = min(self.x_coords)
        self.x_max = max(self.x_coords)
        self.y_min = min(self.y_coords)
        self.y_max = max(self.y_coords)

    def process(self, n_iter, n_pop):
        pop = self.generate_random_population(n_pop)
        for _i in range(0, n_iter):
            pop = self.calculate_next_pop(pop)
        return min(pop, key= lambda tup: tup[2])
        
    def generate_random_population(self, n_pop):
        pop_x = random.sample(set(self.x_coords), n_pop)
        pop_y = random.sample(set(self.y_coords), n_pop)
        return [(x,y, self.z_function(x,y)) for x,y in zip(pop_x , pop_y)]

    def calculate_next_pop(self, pop):
        next_pop = []
        for firefly in pop:
            new_firefly = firefly
            for another_firefly in pop:
                if another_firefly[2] < firefly[2]:
                    new_firefly = self.move_firefly(firefly, another_firefly)
            next_pop.append(new_firefly)
        return next_pop
    
    def move_firefly(self, ori, dest):
        new_x = ori[0] + self.attractiveness_null_distance*math.exp(-self.light_absortion_coefficient*((ori[0] - dest[0]) **2)) *(dest[0] - ori[0]) + self.alpha*random.uniform(0,1)
        new_y = ori[1] + self.attractiveness_null_distance*math.exp(-self.light_absortion_coefficient*((ori[1] - dest[1]) ** 2))*(dest[1] - ori[1]) + self.alpha*random.uniform(0,1)
        new_x = min(max(new_x, self.x_min), self.x_max)
        new_y = min(max(new_y, self.y_min), self.y_max)
        return (new_x, new_y, self.z_function(new_x, new_y))
