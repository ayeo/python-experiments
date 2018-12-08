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


def update(i):
    global cities, current, temperature

    changed = False
    new_solution = swap(cities)
    energy = evaluate(new_solution)
    if accept_solution(current, energy, temperature):
        cities = new_solution
        current = energy
        changed = True

    temperature *= 1 - cooling_factor

    if temperature < 0.01:
        return plt

    if changed is False:
        return update(i)

    plt.cla()
    plt.axis('off')
    plt.text(0, 0, round(temperature, 2))
    plt.plot(cities[:, 0], cities[:, 1], color='red', zorder=0)
    plt.scatter(cities[:, 0], cities[:, 1], marker='o')

    return plt


cities_number = 12
temperature = 200
cooling_factor = .01
cities = (np.random.rand(cities_number, 2) * 100).astype(int)
current = evaluate(cities)

from matplotlib import animation, rc
rc('animation', html='html5')
fig, ax = plt.subplots()
fig.set_tight_layout(True)
writer=animation.FFMpegWriter(bitrate=15000)
anim = animation.FuncAnimation(fig, update, interval=1, frames=500)
anim.save('annealing.mp4',  writer=writer)

