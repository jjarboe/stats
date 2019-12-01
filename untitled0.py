# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 17:40:01 2019

@author: Kaitlin

1. Take sample of random numbers. size = 30
2. take mean
3. add mean to new list
4. repeat 500 times
"""

import numpy as np
import matplotlib.pyplot as plt

avg = []
sample = [0,0,0,0,0,1,1,1,1,1]

for i in range(5):
    #list = []
    total = 0
    '''for j in range(1,30):
        list.append(np.random.choice(np.arange(2,1), p=[0.2,0.8]))
        total += list[j-1]'''
    list = np.random.choice(2,30, p=[.2,.8])
    avg.append(sum(list)/30)
    print(list)
print(avg)

'''#sns.kdeplot(avg)
#sns.distplot(avg)


data = np.random.choice(np.arange(1, 7), p=[0.1, 0.05, 0.05, 0.2, 0.4, 0.2])
bins = np.arange(13)-0.5

plt.figure(figsize=(10,30))

hist, edges = np.histogram(avg, bins=bins)

y = np.arange(1,hist.max()+1)
x = np.arange(12)
X,Y = np.meshgrid(x,y)

p = plt.scatter(X,Y, c=Y<=hist, cmap="Greys")

p.figure.savefig("graph")

plt.show()
'''