import random


class DifferentialAlgorithm:
    def __init__(self, x,y,z, iterations = 1000, population_size = 100):
        self.x = x
        self.y = y
        self.z = z
        self.iterations = iterations
        self.pop_size = population_size

    def diferential_algorithm(self):
        population = self.generate_initial_population()
        for _ in range(0, self.iterations):
            population = self.next_generation(population)

        minimum = min(population, key = lambda t: self.z(t[0], t[1]))
        return (minimum[0], minimum[1], self.z(minimum[0], minimum[1]))


    def generate_initial_population(self):
        population = []
        copy_x = list(self.x)
        copy_y = list(self.y)
        for _ in range(0, self.pop_size):
            value_x = random.choice(copy_x)
            value_y = random.choice(copy_y)
            value_z = self.z(value_x, value_y)

            population.append((value_x, value_y, value_z))

            copy_x.remove(value_x)
            copy_y.remove(value_y)

        return population


    def next_generation(self, pop):
        population = []

        for individual in pop:
            ind1,ind2,ind3 = self.select_mutated(individual, pop)
            noisy_vector = self.mutation(ind1,ind2,ind3)
            test_vector = self.crossover(individual, noisy_vector)           
            new_individual = self.compete(individual, test_vector)
            population.append(new_individual)
        
        return population


    def select_mutated(self, individual, pop):
        population = list(pop)
        population.remove(individual)

        ind1 = random.choice(population)
        population.remove(ind1)

        ind2 = random.choice(population)
        population.remove(ind2)

        ind3 = random.choice(population)
        population.remove(ind3)
        
        return ind1,ind2,ind3


    def mutation(self, ind1, ind2, ind3):
        F = 0.5
        intermediary = tuple( F * (ind2[i] - ind1[i]) for i in range(0, len(ind1)))
        final = tuple(intermediary[i] + ind3[i] for i in range(0, len(ind1)))

        return final

    def crossover(self, individual, noisy_vector):
        CR = 0.8

        test_array = [None for i in range(0, len(individual))]
        j = random.randint(0, len(individual))
        for i in range(0, len(individual)):
            random_param = random.uniform(0,1)
            if random_param < CR or j == i:
                test_array[i] = noisy_vector[i]
            else:
                test_array[i] = individual[i]

        test_vector = tuple(test_array)
        return test_vector

    def compete(self, old_individual, new_individual):
        x_individual = new_individual[0]
        y_individual = new_individual[1]
        
        x_old_individual = old_individual[0]
        y_old_individual = old_individual[1]

        return new_individual if (self.z(x_individual, y_individual) <=  self.z(x_old_individual, y_old_individual)) else old_individual
