#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import animation, rc
from collections import Counter
from random import randint

rc('animation', html='html5')

width = 250
height = 250
population = 5000
deadZone = 5
edenMargin = 50
cmap = 'hot'

fig, ax = plt.subplots()
fig.set_tight_layout(True)

def get_color():
    if get_color.color > 100:
        get_color.color = 30

    get_color.color += 0.5
    return get_color.color    
        
get_color.color = 30;

def neighbors(cell):
    (x, y) = cell
    return [(x-1, y-1), (x, y-1), (x+1, y-1), 
            (x-1, y),             (x+1, y), 
            (x-1, y+1), (x, y+1), (x+1, y+1)]
    
def neighbor_counts(world):
    return Counter(nb for cell in world 
                      for nb in neighbors(cell))
    
def translate(world):
    universe = np.full((width, height), 0)
    nnn = neighbor_counts(world)
    #color = get_color()
    for item in world:
        universe[item[0], item[1]] = nnn[item[0], item[1]] * 12
    return universe.transpose((1, 0))    


world = []

for x in np.arange(population):
    world.append((randint(edenMargin, width - edenMargin), randint(edenMargin, height - edenMargin)))

ax.imshow(translate(world), cmap=cmap, vmin=0, vmax=100)
plt.axis('off')

def filter(world):
 for item in world:
     if item[0] > width - deadZone or item[0] < deadZone:
         world.remove(item)
         
     if item[1] > height - deadZone or item[1] < deadZone:
         world.remove(item)         
         

def next_generation(world):
    possible_cells = counts = neighbor_counts(world)
    return {cell for cell in possible_cells
            if (counts[cell] == 3) 
            or (counts[cell] == 2 and cell in world)}

def update(num):
    global world

    plt.cla()
    world = next_generation(world)        
    filter(world)
    ax.imshow(translate(world), cmap=cmap, vmin=0, vmax=100)
    plt.axis('off')
    return plt

writer=animation.FFMpegWriter(bitrate=15000)
anim = animation.FuncAnimation(fig, update, interval=200, frames=50)
#anim.save('game-of-life.mp4',  writer=writer)
plt.show()

    



