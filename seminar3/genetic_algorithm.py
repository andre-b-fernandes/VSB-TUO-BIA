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
        total_fitness = self.calculate_total_fitness(population)
        population = self.set_bounds(population, total_fitness)
        chosen_parents = self.parents_for_breeding(population)
        children = self.generate_children(chosen_parents)
        children = self.mutation(children)
        children = self.elitism(population, children)
        return children

    def calculate_total_fitness(self, population):
        total_fitness = 0
        for ind in population:
            total_fitness += ind.fitness
        return total_fitness

    def set_bounds(self, population, total_fitness):
        accum = 0
        for ind in population:
            ind.set_bounds(accum, total_fitness)
            accum = ind.upper_bound
        return population

    def elitism(self, population, children):
        population.sort()
        children.sort()
        i = 0
        while len(children) < len(population):
            children.append(population[i])
            i += 1
        return children

    def parents_for_breeding(self, population):
        pop = []
        c = 0
        while c < len(population):
            r = random.uniform(0, 1)
            if r <= population[c].lower_bound or r > population[c].upper_bound:
                pop.append(population[c])
            c += 1
        return pop

    def generate_children(self, population):
        children = []
        for i in range(0, len(population) - 1):
            children.append(population[i].crossover(population[i + 1]))
        return children

    def mutation(self, population):
        alfa = 0.9
        for ind in population:
            r = random.uniform(0,1)
            if r > alfa:
                ind.mutate()
        return population
    
    def algorithm(self, pop_size, n_iterations):
        pop = self.generate_initial_population(pop_size)
        for i in range(0, n_iterations):
            pop = self.selection(pop)
            min_iter = min(pop)
            print("Iteration: " + str(i) + " with fitness " + str(min_iter.fitness))
        return min(pop)
