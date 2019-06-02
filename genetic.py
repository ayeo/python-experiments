import random
import numpy as np


def init_random_population(population_size, genome_length):
    integers = np.arange(0, genome_length).astype(int)
    population = np.empty((population_size, genome_length)).astype(int)
    for i in range(population_size):
        genome = integers.copy()
        random.shuffle(genome)
        population[i] = genome

    return population


def evaluate(points):
    distance = 0
    a = cities[0]
    for index in range(0, len(points)):
        b = cities[points[index]]
        distance += np.linalg.norm(a - b)
        a = b

    return distance




cities = (np.random.rand(10, 2) * 100).astype(int)
solutions = init_random_population(10, 5)

solutions = sorted(solutions, key=lambda x: evaluate(x))


print(evaluate(solutions[0]))
print(evaluate(solutions[1]))
print(evaluate(solutions[2]))
print(evaluate(solutions[3]))
print(evaluate(solutions[4]))

# y = np.asarray([10, 10])
# x = np.asarray([0, 0])
#
# print(np.linalg.norm(x - y))

