# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 17:40:01 2019

@author: Kaitlin

1. Take sample of random numbers. size = 30
2. take mean
3. add mean to new list
4. repeat >200 times
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import pandas as pd


'''Default values'''
#Probability
p = .5
#Number of trials
n = 1000
#Size of bins in percent integer
b = 5
#Size of trials
t = 50


'''Deal with command line arguments'''
if(len(sys.argv)):
    for i in range(1,len(sys.argv)):
        #Probability
        if sys.argv[i][0]=='p':
            p = float(sys.argv[i][2:])
            print(p)
        #Number of Trials
        elif sys.argv[i][0]=='n':
            n = int(sys.argv[i][2:])
            print(n)
        #Size of bins
        elif sys.argv[i][0]=='b':
            b = float(sys.argv[i][2:])
            print(b)
        #Size of trials
        elif sys.argv[i][0]=='t':
            t = int(sys.argv[i][2:])
            print(t)
        #Seed for trial generation
        elif sys.argv[i][0]=='s':
            s = int(sys.argv[i][2:])
            np.random.seed(s)
        #error if not any of these
        else:
            raise ValueError(sys.argv[i],' is not a valid argument.')
        

'''Take the random sample'''
avg = []
for i in range(n):
    list = np.random.choice(2,t, p=[(1-p),p])
    avg.append(sum(list)*100/t)


'''histogram'''
fig = plt.figure()
ax = sns.distplot(pd.Series(avg,name="Percent who Said 'Yes'"))
ax.figure.savefig("histogram")
ax.clear()


'''dotplot :('''
#number of bins
bins = np.arange((100.0/b)+2)*b

#figure scaling, axis labels, and ticks
p = plt.figure(figsize=(10,20))
ax = plt.axes()
ax.xaxis.set_major_locator(ticker.MultipleLocator(b/50))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(b/100))
p.add_axes(ax)
p.suptitle('Distribution of Averages', fontsize=20)
plt.xlabel('Proportion', fontsize=18)
plt.ylabel('Frequency', fontsize=18)

#set up and set frequency and value tables
hist, edges = np.histogram(avg,bins=bins,)#range=(0,10))
y = np.arange(1,hist.max()+1)
x = np.arange((100.0/b)+1)/(100.0/b)
X,Y = np.meshgrid(x,y)

#plot the points
plt.scatter(X,Y, c=Y<=hist, cmap="Greys",s=1)

#save the figure to dot.png
p.savefig("dot")