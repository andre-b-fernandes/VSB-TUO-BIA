import random, math

class Soma:
    def __init__(self, x_coords, y_coords, z_function, n_iter, pop_size):
        self.number_iterations = n_iter
        self.population_size = pop_size
        self.z = z_function
        self.x = x_coords
        self.y = y_coords
        self.PRT = 0.5
        self.STEP = 0.11

    def generate_initial_population(self):
        dimension = min(len(self.x), len(self.y), self.population_size)
        copy_x = list(self.x)
        copy_y = list(self.y)
        population = []
        for i in range(0, dimension):
            x_choice = random.choice(copy_x)
            y_choice = random.choice(copy_y)
            copy_x.remove(x_choice)
            copy_y.remove(y_choice)
            population.append((x_choice, y_choice, self.z(x_choice, y_choice)))   

        self.best = min(population, key= lambda x: x[len(x) - 1])
        return population

    def calculate_prt_vector(self, dimension):
        prt_vector = [ int(random.uniform(0,1) > self.PRT) for i in range(0, dimension)]
        return tuple(prt_vector)

    def calculate_steps(self, individual):
        prt_vector = self.calculate_prt_vector(len(individual) - 1)
        difference_list = [ (self.best[i] - individual[i]) * prt_vector[i] for i in range(0, len(prt_vector))]
        steps_x = int(round(difference_list[0]/self.STEP))
        steps_y = int(round(difference_list[1]/self.STEP))
        return steps_x, steps_y

    def calculate_next_coords(self, individual):
        max_domain_x, min_domain_x = max(self.x), min(self.x)
        max_domain_y, min_domain_y = max(self.y), min(self.y)
        steps_x, steps_y = self.calculate_steps(individual)
        new_x_list = [individual[0]] + [ min(max(individual[0] + self.STEP*i*int(steps_x/abs(steps_x)), min_domain_x), max_domain_x) for i in range(1, abs(steps_x))]
        new_y_list = [individual[1]] + [ min(max(individual[1] + self.STEP*i*int(steps_y/abs(steps_y)), min_domain_y), max_domain_y) for i in range(1, abs(steps_y))]
        pairs = list(map(lambda x,y: (x,y, self.z(x,y)) , new_x_list, new_y_list))
        return min(pairs, key=lambda x: x[len(x) - 1])
    
    def calculate_next_population(self, pop):
        population = [self.calculate_next_coords(individual) for individual in pop]
        self.best = min(population, key=lambda x: x[len(x) - 1])
        return population

    def soma_algorithm(self):
        pop = self.generate_initial_population()
        for _i in range(0, self.number_iterations):
            pop = self.calculate_next_population(pop)
        return self.best

        

            
        



        
        
        
    
    
    


