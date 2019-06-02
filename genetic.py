import random
import numpy as np


def init_random_population():
    integers = np.arange(0, genome_length).astype(int)
    population = np.empty((population_size, genome_length)).astype(int)
    for i in range(population_size):
        genome = integers.copy()
        random.shuffle(genome)
        population[i] = genome

    return population


def evaluate(points):
    distance = 0
    a = cities[0]  # always start form first city
    for index in range(0, len(points)):
        b = cities[points[index]]
        distance += np.linalg.norm(a - b)
        a = b
    distance += np.linalg.norm(b - cities[0])  # go back to starting point

    return distance


population_size = 10
genome_length = 10
cities = (np.random.rand(population_size, 2) * 100).astype(int)
solutions = init_random_population()

solutions = sorted(solutions, key=lambda x: evaluate(x))

#  make sure it is sorted
print(evaluate(solutions[0]))
print(evaluate(solutions[1]))
print(evaluate(solutions[2]))
print(evaluate(solutions[3]))
print(evaluate(solutions[4]))
print(evaluate(solutions[5]))
print(evaluate(solutions[6]))
print(evaluate(solutions[7]))
print(evaluate(solutions[8]))
