import numpy as np
import matplotlib.pyplot as plt
import random
import math

def evaluate(cities):
    distance = 0
    for index in range(len(cities)):
        if index == len(cities)-1:
            a = cities[index]
            b = cities[0]
        else:
            a = cities[index]
            b = cities[index + 1]

        distance += np.linalg.norm(a - b)
        index += 1

    return distance


def swap(x):
    y = np.copy(x)
    i = random.randint(0, len(x) - 1)
    j = random.randint(0, len(x) - 1)
    y[i], y[j] = x[j], x[i]

    return y


def accept_solution(solution1, solution2, temperature):
    energy1 = evaluate(solution1)
    energy2 = evaluate(solution2)
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
    while temperature > 0.001:
        new_solution = swap(cities)
        if accept_solution(cities, new_solution, temperature):
            cities = new_solution

        temperature *= 1 - cooling_factor

    return cities

cities = process(25)
plt.plot(cities[:, 0], cities[:, 1], color='red', zorder=0)
plt.scatter(cities[:, 0], cities[:, 1], marker='o')
plt.axis('off')
plt.show()