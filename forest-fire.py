#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from random import randint

fig, ax = plt.subplots()

items = ('empty', 'tree', 'fire')
width = 100
height = 100
forest = np.full((width, height), 0)

def breedTrees():
    for y in range(height):
        for x in range(width):
            if randint(0, 50) == 5:
                forest[x, y] = 1

def neighbors(cell):
    (x, y) = cell
    return [(x-1, y-1), (x, y-1), (x+1, y-1), 
            (x-1, y),             (x+1, y), 
            (x-1, y+1), (x, y+1), (x+1, y+1)]
    
def count_neighbors(cell, itemType):
    counter = 0;
    
    for xxx in neighbors(cell):
        if not (xxx[0] >= width or xxx[1] >= height):
            if forest[xxx] == itemType:
                counter += 1
    return counter

def get_neighbors_map(itemType):
    result = np.zeros((width, height))
    for y in range(height):
        for x in range(width):
            result[x, y] = count_neighbors((x, y), itemType)
    return result
    
def spawn():
    neighbors_map = get_neighbors_map(2)
    for y in range(height):
        for x in range(width):
            if (forest[x, y] == 2):
                forest[x, y] = 0
                
            if (neighbors_map[x, y] > 0 and forest[x, y] == 1):
                forest[x, y] = 2;
                
def ignite():
    if randint(0, 10) == 5:
        forest[randint(0, width), randint(0, height)] = 2;
                    

N = 10
colors = [(0.0, 0.0, 0.0),(0.0, 0.6, 0.2),(1.0, 0.0, 0.0)]
colors.extend(mpl.cm.jet(np.linspace(0, 1, N-1)))
cmap = mpl.colors.ListedColormap(colors)                       
        
def update(num):
    breedTrees()
    ignite();
    spawn()
    plt.cla()
    ax.imshow(forest, cmap=cmap, vmin=0, vmax=N-1)
    plt.axis('off')
    return plt


ax.imshow(forest, cmap=cmap)
plt.axis('off')            

writer=animation.FFMpegWriter(bitrate=15000)
anim = animation.FuncAnimation(fig, update, interval=10, frames=100)
anim.save('forest-fire.mp4',  writer=writer)
#plt.show()
