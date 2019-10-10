import random

class Individual:

    def __init__(self, chromossomes):
        self.chromossomes = chromossomes
        self.fitness = self.calculate_fitness()

    def print_chromossomes(self):
        print("My fitness : " + str(self.fitness))
        for chro in self.chromossomes:
           chro.print()

    def calculate_fitness(self):
        fitness = self.chromossomes[0].distance(self.chromossomes[len(self.chromossomes) - 1]) # Last to the first
        i = 0
        for i in range(len(self.chromossomes) - 1):
            fitness += self.chromossomes[i].distance(self.chromossomes[i + 1])
        return fitness

    
    def set_probability(self, probability):
        self.probability = self.fitness/probability

    def crossover(self, individual):
        r = random.randint(0, len(self.chromossomes) - 1)
        chroms = self.chromossomes
        self_chromossome = self.chromossomes[r]
        other_chromossome = individual.chromossomes[r]
        for i in range(0, len(self.chromossomes)):
            if self.chromossomes[i] == other_chromossome:
                chroms[i] = self_chromossome
                break
        chroms[r] = other_chromossome
        return Individual(chroms)

    def mutate(self):
        options = list(range(0, len(self.chromossomes)))
        first = random.choice(options)
        options.remove(first)
        second = random.choice(options)
        tmp = self.chromossomes[first]
        self.chromossomes[first] = self.chromossomes[second]
        self.chromossomes[second] = tmp
        self.fitness = self.calculate_fitness()


    def __gt__(self, individual):
        return self.fitness > individual.fitness

    def __eq__(self, individual):
        return self.fitness == individual.fitness
    
    def __lt__(self, individual):
        return self.fitness < individual.fitness

    def __le__(self, individual):
        return self.fitness <= individual.fitness
    
    def __ge__(self, individual):
        return self.fitness >= individual.fitness
