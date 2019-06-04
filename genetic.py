import math
import random

import matplotlib.pyplot as plt
import numpy as np

elite = 5
matingPoolSize = 50
genome_length = 20
stability_factor = 100
breeding_intensity = 50


def init_random_population():
    integers = np.arange(0, genome_length).astype(int)
    population = np.empty((matingPoolSize, genome_length)).astype(int)
    for i in range(matingPoolSize):
        genome = integers.copy()
        random.shuffle(genome)
        population[i] = genome

    return np.array(population)


def evaluate(route):
    distance = 0
    a = cities[route[0]]
    for index in range(1, len(route)):
        b = cities[route[index]]
        distance += np.linalg.norm(a - b)
        a = b
    distance += np.linalg.norm(b - cities[route[0]])  # go back to starting point

    return distance


def crossover(population):
    a = random.randint(0, matingPoolSize - 1)
    b = a
    while (a == b):
        b = random.randint(0, matingPoolSize - 1)
    aGenomeLength = math.floor(genome_length/2)
    firstPart = population[a][:aGenomeLength]
    secondPart = np.array([n for n in population[b] if n not in firstPart])
    x1 = np.append(firstPart, secondPart)

    firstPart = population[b][:aGenomeLength]
    secondPart = np.array([n for n in population[b] if n not in firstPart])
    x2 = np.append(firstPart, secondPart)

    return np.vstack([mutate(x1), mutate(x2)])


def randomPair(max):
    a = b = random.randint(0, max)
    while (a == b):
        b = random.randint(0, max)

    return (a, b)


def mutate(genome):
    (a, b) = randomPair(genome_length - 1)
    tmp = genome[a]
    genome[a] = genome[b]
    genome[b] = tmp

    return genome


def evolve(population):
    last = evaluate(population[0])
    counter = 0

    while (True):
        current = evaluate(population[0])
        print(current)
        if (last == current):
            counter = counter + 1
        else:
            last = current
            counter = 0

        if (counter == stability_factor):
            break

        new_population = population[:elite]
        for x in range(breeding_intensity):
            new_population = np.vstack([new_population, crossover(population)])
        new_population = np.array(sorted(new_population, key=lambda x: evaluate(x)))
        population = new_population[:matingPoolSize]


    return population


# solution
cities = (np.random.rand(genome_length, 2) * 100).astype(int)
population = init_random_population()
population = evolve(population)


# printing result (mapping and plot)
solution = np.empty((genome_length+1, 2)).astype(int)
x = 0
for i in population[0]:
    solution[x] = cities[i]
    x += 1
solution[genome_length] = cities[population[0][0]]


plt.plot(solution[:, 0], solution[:, 1], color='green', zorder=0)
plt.scatter(cities[:, 0], cities[:, 1], color='red', marker='o')
plt.axis('off')
plt.show()

exit(0)