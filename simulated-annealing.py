import numpy as np
import matplotlib.pyplot as plt
import random
import math


def evaluate(cities):
    distance = 0
    for index in range(len(cities)):
        a = cities[index]
        if index == len(cities) - 1:
            b = cities[0]
        else:
            b = cities[index + 1]

        distance += np.linalg.norm(a - b)
        index += 1

    return distance


def swap(x):
    i = random.randint(0, len(x) - 2)
    j = random.randint(i, len(x) - 1)

    y = np.copy(x)
    y[i: j] = y[i: j][::-1]

    return y


def accept_solution(energy1, energy2, temperature):
    if energy1 > energy2:
        return True
    else:
        a = math.exp((energy1 - energy2) / temperature)
        b = random.random()
        if a > b:
            return True
        else:
            return False


def process(cities_number, temperature = 800, cooling_factor = .001):
    cities = (np.random.rand(cities_number, 2) * 100).astype(int)
    current = evaluate(cities)

    while temperature > 0.001:
        new_solution = swap(cities)
        energy = evaluate(new_solution)
        if accept_solution(current, energy, temperature):
            cities = new_solution
            current = energy

        temperature *= 1 - cooling_factor

    return cities

cities = process(50, temperature = 3000)
plt.plot(cities[:, 0], cities[:, 1], color='red', zorder=0)
plt.scatter(cities[:, 0], cities[:, 1], marker='o')
plt.axis('off')
plt.show()