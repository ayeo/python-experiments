# Outstanding simple approach with genetic algorithm.
# The solution provides quite good result quality while it is simple and quick
# (despite using simplified crossing over algorithm)
# @link https://github.com/ayeo/python-experiments/blob/master/genetic.png

import math
import random

import matplotlib.pyplot as plt
import numpy as np

cities_number = 20
elite_size = 5
mating_pool_size = 50
breeding_intensity = 50
stability_factor = 100


def init_population() -> list:
    genes = list(range(cities_number))
    population = []
    for i in range(mating_pool_size):
        g = genes.copy()
        random.shuffle(g)
        population.append(g)
    return population


def total_route_distance(route: list) -> float:
    distance = 0
    a = cities[route[0]]
    for index in range(1, len(route)):
        b = cities[route[index]]
        distance += np.linalg.norm(a - b)
        a = b
    distance += np.linalg.norm(b - cities[route[0]])  # go back to starting point
    return distance


def cross_genomes(a: list, b: list) -> list:
    aGenomeLength = math.floor(cities_number / 2)
    first = a[slice(aGenomeLength)]
    second = [n for n in b if n not in first]
    return first + second


def crossover(population: list) -> list:
    (a, b) = random_pair(mating_pool_size - 1)
    return \
        [mutate(cross_genomes(population[a], population[b]))] + \
        [mutate(cross_genomes(population[b], population[a]))]


def random_pair(max: int) -> (int, int):
    a = b = random.randint(0, max)
    while (a == b):
        b = random.randint(0, max)
    return (a, b)


def mutate(genome: list) -> list:
    (a, b) = random_pair(cities_number - 1)
    genome[a], genome[b] = genome[b], genome[a]
    return genome


def evolve(population: list) -> list:
    last = total_route_distance(population[0])
    counter = 0
    while (counter != stability_factor):
        current = total_route_distance(population[0])
        print(current)
        if (last == current):
            counter = counter + 1
        else:
            last = current
            counter = 0
        new_population = population[:elite_size]
        for x in range(breeding_intensity):
            new_population = new_population + crossover(population)
        new_population = sorted(new_population, key=lambda x: total_route_distance(x))
        population = new_population[:mating_pool_size]
    return population


# solution
cities = (np.random.rand(cities_number, 2) * 100).astype(int)
population = init_population()
population = evolve(population)


# printing result (mapping and plot)
solution = []
x = 0
for i in population[0]:
    solution.append(cities[i])
    x += 1
solution.append(cities[population[0][0]])
xx = [row[0] for row in solution]
yy = [row[1] for row in solution]
plt.plot(xx, yy, color='green', zorder=0)
plt.scatter(cities[:, 0], cities[:, 1], color='red', marker='o')
plt.axis('off')
plt.show()

exit(0)