# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 17:40:01 2019

@author: Kaitlin

1. Take sample of random numbers. size = 30
2. take mean
3. add mean to new list
4. repeat 500 times
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print(str(sys.argv))

p = float(sys.argv[1])
n = int(sys.argv[2])
avg = []

for i in range(n):
    list = np.random.choice(2,30, p=[(1-p),p])
    avg.append(sum(list)/3.0)
    #print(list)
print(avg)

#sns.kdeplot(avg)
sns.distplot(avg)


#data = np.random.randint(0,21,size=30)
#print(data)
#bins=np.linspace(0,1,num=20)
bins=np.arange(12)
#[0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1.]
print(bins)

plt.figure(figsize=(10,30))

hist, edges = np.histogram(avg,bins=bins,range=(0,10))

y = np.arange(1,hist.max()+1)
x = np.arange(11)/10.0
X,Y = np.meshgrid(x,y)
print(X)

p = plt.scatter(X,Y, c=Y<=hist, cmap="Greys")

p.figure.savefig("graph")

plt.show()

sys.exit()