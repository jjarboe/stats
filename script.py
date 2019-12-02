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
import pandas as pd


'''Deal with command line arguments'''
p = float(sys.argv[1])
n = int(sys.argv[2])

if(len(sys.argv)==4):
    np.random.seed(sys.argv[3])


'''Take the random sample'''
avg = []
for i in range(n):
    list = np.random.choice(2,30, p=[(1-p),p])
    avg.append(sum(list)/3.0)


'''histogram'''
#sns.kdeplot(avg)
fig = plt.figure()
ax = sns.distplot(pd.Series(avg,name="Percent who Said 'Yes'"))
ax.figure.savefig("histogram")


'''dotplot :('''
#number of bins, scaling and labels
bins = np.arange(12)
fig = plt.figure(figsize=(10,20))
fig.suptitle('Distribution of Averages', fontsize=20)
plt.xlabel('Percentage', fontsize=18)
plt.ylabel('Frequency', fontsize=16)

#make the graph
hist, edges = np.histogram(avg,bins=bins,range=(0,10))

#make y=frequency and x a percentage
y = np.arange(1,hist.max()+1)
x = np.arange(11)/10.0
X,Y = np.meshgrid(x,y)

#plot the points
p = plt.scatter(X,Y, c=Y<=hist, cmap="Greys",s=1)

#save the figure to dot.png
p.figure.savefig("dot")