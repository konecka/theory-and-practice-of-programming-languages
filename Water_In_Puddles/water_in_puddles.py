# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def load(path):
    return list(np.loadtxt(path))

def check(landscape, y, x):
    l = r = False
    
    # проверка соседей слева на наличие "земли"   
    for i in range(x-1, 0, -1):
        if (landscape[y, i] == -2):
            return False
        elif(landscape[y, i] == 0 or landscape[y, i] == -1):
            l = True
            break
    # проверка соседей справа на наличие "земли"     
    for i in range(x+1, landscape.shape[1]):
        if (landscape[y, i] == -2):
            return False
        elif(landscape[y, i] == 0 or landscape[y, i] == -1):
            r = True
            break
    return (l and r)

def get_water_blocks(landscape, slandscape, max_height, l_height, r_height):
    
    water_blocks = 0 
    
    landscape[0:max_height-l_height+1, 0] = -2
    landscape[0:max_height-r_height, len(slandscape)-1] = -2

    for y in range(1, landscape.shape[1]):
        index = 0
        for col in slandscape[1:-1]:
            index +=1
            if(col[0] == y):
                if(max_height-int(col[0])-1 >= 0):
                    if(check(landscape, max_height-int(col[0])-1, col[1])):
                        landscape[max_height-int(col[0]) -1, col[1]] = -1
                        slandscape[index][0] +=1
                        water_blocks += 1                        
                    else:
                        landscape[max_height-int(col[0]) -1, col[1]] = -2
                        slandscape[index][0] +=1
    return water_blocks

if __name__ == "__main__":

    cols = load("data/landscape.txt")
    
    # самая высокая часть острова
    max_height = int(max(cols))
    
    #высота левого столбца
    l_height = int(cols[1])
    
    #высота правого столбца
    r_height = int(cols[-1])
    
    landscape = np.ones((max_height, len(cols)))
    
    i=0
    for col in cols:
        landscape[max_height - int(col):max_height, i] = 0
        i+= 1
    
    slandscape = []    
    for i in range(len(cols)):
        slandscape.append([cols[i], i])
    
    
    water_blocks = get_water_blocks(landscape, slandscape, max_height, l_height, r_height)
    
    print(water_blocks)
    
    plt.figure(1)
    plt.imshow(landscape)
    plt.show()