import random, math, copy
from functools import reduce

class TeachingLearningOptimization:
    
    def __init__(self, x, y ,z):
        self.x_coords = x
        self.y_coords = y
        self.z_function = z
        self.x_min = min(self.x_coords)
        self.x_max = max(self.x_coords)
        self.y_min = min(self.y_coords)
        self.y_max = max(self.y_coords)

    def process(self, n_iterations, n_pop):
        pop = self.generate_initial_pop(n_pop)
        for _i in range(0, n_iterations):
            teacher = self.calculate_best_of_population(pop)
            mean = self.mean_population(pop)
            pop = self.calculate_next_pop(teacher, pop , mean)
        return min(pop, key= lambda x: x[2])
            
                        
    def generate_initial_pop(self, n_pop):
        x = random.sample(set(self.x_coords), n_pop)
        y = random.sample(set(self.y_coords), n_pop)
        return [ (x_coord, y_coord, self.z_function(x_coord, y_coord) ) for x_coord,y_coord in zip(x,y) ]
        
    def calculate_best_of_population(self, pop):
        return max(pop, key= lambda element: element[2])

    def mean_population(self, pop):
        l = list(map(lambda element: element/len(pop), reduce(lambda x,y: (x[0]+y[0], x[1] + y[1]), pop)))
        l.append(self.z_function(l[0], l[1]))
        return tuple(l)

    def calculate_next_pop(self, teacher, pop, mean):
        pop_without_teacher = list(set(pop) - set({teacher}))
        for i in range(0, len(pop_without_teacher)):
            pop_without_teacher[i] = self.teacher_phase(pop_without_teacher[i], teacher, mean)
            pop_without_teacher[i] = self.learner_phase(pop_without_teacher[i], pop_without_teacher)
        return pop_without_teacher + [teacher]
            
    def teacher_phase(self, learner, teacher, mean):
        tf = round(1 + random.uniform(0,1))
        new_x = learner[0] + random.uniform(0,1) * (teacher[0] - tf * mean[0])
        new_y = learner[1] + random.uniform(0,1) * (teacher[1] - tf * mean[1])
        new_x = min(max(new_x, self.x_min), self.x_max)
        new_y = min(max(new_y, self.y_min), self.y_max)
        new_z = self.z_function(new_x, new_y)
        if new_z < learner[2]:
            return (new_x, new_y, new_z)
        else:
            return learner

    def learner_phase(self, learner, learners):
        another_learner = random.choice(list(set(learners) - set({learner})))
        new_x, new_y = learner[0], learner[1]
        if learner[2] <= another_learner[2]:
            new_x = learner[0] + random.uniform(0,1) * (learner[0] - another_learner[0])
            new_y = learner[1] + random.uniform(0,1) * (learner[1] - another_learner[1])
        else:
            new_x = learner[0] + random.uniform(0,1) * (another_learner[0] - learner[0])
            new_y = learner[1] + random.uniform(0,1) * (another_learner[1] - learner[1])   
        new_x = min(max(new_x, self.x_min), self.x_max)
        new_y = min(max(new_y, self.y_min), self.y_max)
        return (new_x, new_y, self.z_function(new_x, new_y))
    

