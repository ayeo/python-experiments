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


def evaluate(route):
    distance = 0
    a = cities[route[0]]
    for index in range(1, len(route)):
        b = cities[route[index]]
        distance += np.linalg.norm(a - b)
        a = b
    distance += np.linalg.norm(b - cities[route[0]])  # go back to starting point

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
            mutate(),
        ]])
        population = np.array(sorted(population, key=lambda x: evaluate(x)))
        population = population[:population_size]


    return population


population_size = 10
genome_length = 8
generations = 25
cities = (np.random.rand(genome_length, 2) * 100).astype(int)
population = init_random_population()
population = evolve(population)



# print result
solution = np.empty((genome_length+1, 2)).astype(int)
x = 0
for i in population[0]:
    solution[x] = cities[i]
    x += 1
solution[genome_length] = cities[population[0][0]]


plt.plot(solution[:, 0], solution[:, 1], color='red', zorder=0)
plt.scatter(cities[:, 0], cities[:, 1], marker='o')
plt.axis('off')
plt.show()

exit(0)