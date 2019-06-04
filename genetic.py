import random
import numpy as np
import math
import matplotlib.pyplot as plt


def init_random_population():
    integers = np.arange(0, genome_length).astype(int)
    population = np.empty((population_size, genome_length)).astype(int)
    for i in range(population_size):
        genome = integers.copy()
        random.shuffle(genome)
        population[i] = genome

    return np.array(population)


def evaluate(points):
    distance = 0
    a = cities[0]  # always start form first city
    for index in range(0, len(points)):
        b = cities[points[index]]
        distance += np.linalg.norm(a - b)
        a = b
    distance += np.linalg.norm(b - cities[0])  # go back to starting point

    return distance


def crossover():
    a = random.randint(0, population_size - 1)
    b = a
    while (a == b):
        b = random.randint(0, population_size - 1)
    aGenomeLength = math.floor(genome_length/2)
    firstPart = population[a][:aGenomeLength]
    secondPart = np.array([n for n in population[b] if n not in firstPart])

    return np.append(firstPart, secondPart)

def mutate():
    i = random.randint(0, population_size - 1)
    a = random.randint(0, genome_length - 1) #extract this to method
    b = a
    while (a == b):
        b = random.randint(0, genome_length - 1)
    genome = population[i]

    tmp = genome[a]
    genome[a] = genome[b]
    genome[b] = tmp

    return genome

def evolve(population):
    for i in range(generations):
        print(evaluate(population[0]))
        population = np.vstack([population, [
            crossover(),
            crossover(),
            crossover(),
            mutate(),
            mutate(),
            mutate()
        ]])
        population = np.array(sorted(population, key=lambda x: evaluate(x)))
        population = population[:population_size]


    return population


population_size = 10
genome_length = 5
generations = 50
cities = (np.random.rand(genome_length, 2) * 100).astype(int)
population = init_random_population()
population = evolve(population)

solution = np.empty((genome_length, 2)).astype(int)
for i in population[0]:
    solution[i] = cities[i]


plt.plot(solution[:, 0], solution[:, 1], color='red', zorder=0)
plt.scatter(cities[:, 0], cities[:, 1], marker='o')
plt.axis('off')
plt.show()

exit(0)