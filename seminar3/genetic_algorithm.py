import random
from individual import Individual

class GeneticAlgorithm:

    def __init__(self, chromossomes):
        self.chromossomes = chromossomes

    def print_pop(self, population):
        for ind in population:
            print("\tIndividual\r\n")
            ind.print_chromossomes()              
            

    def generate_initial_population(self, population_length):
        i = 0
        pop = []
        while i < population_length:
            chro = set(range(0, len(self.chromossomes)))
            individual = []
            while len(chro) > 0:
                r = random.choice(list(chro))
                chromossome = self.chromossomes[r]
                individual.append(chromossome)
                chro.remove(r)
            pop.append(Individual(individual))
            i += 1
        return pop
        

    def selection(self, population):
        pop_size = len(population)
        total_fitness = 0 
        for ind in population:
            total_fitness += ind.fitness

        for ind in population:
            ind.set_probability(total_fitness)

        deleted = []
        c = 0
        while c < len(population):
            r = random.uniform(0,1)
            if r > population[c].probability:
                deleted.append(population[c])
                del population[c]
                c -= 1
            c += 1

        children = []
        for i in range(0, len(population) - 1):
            children.append(population[i].crossover(population[i + 1]))

        deleted.sort(reverse = True)
        pop = population + children
        while len(pop) < pop_size:
            pop.append(deleted.pop(0))

        return pop
    
    def mutation(self, population):
        alfa = 0.8
        for ind in population:
            r = random.uniform(0,1)
            if r > alfa:
                ind.mutate()
        pass
        return population
    
    def algorithm(self, pop_size, n_iterations):
        pop = self.generate_initial_population(pop_size)
        for i in range(0, n_iterations):
            pop = self.selection(pop)
            pop = self.mutation(pop)
        return max(pop)