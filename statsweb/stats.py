"""
Created on Fri Nov 29 17:40:01 2019

@author: Kaitlin

1. Take sample of random numbers. size = 30
2. take mean
3. add mean to new list
4. repeat >200 times
"""


'''
1. Import necessary libraries
2. Set default variables
3. Use user-imputted values for variables if applicible
4. Take the sample
5. Create and output graphs
6. Output statistical data
'''

''' Libraries'''
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import pandas as pd
import math


'''
Description: Sets default values for variables
Params: None
Output: list values containing the mean, number of trials, size of bins, and size of trials
'''
def initialize():
    #Probability
    p = 5.0
    #Number of trials
    n = 1000
    #Size of bins in percent integer
    b = 0.5
    #Size of trials
    t = 50
    #Create a list with core values
    values = [p, n, b, t]
    return values


'''
Description: Creates a random sample
Params: p, n, t
Output: list avg
'''
def sample(p, n, t):
    avg = []
    for i in range(n):
        list = np.random.choice(2,t, p=[(1-(p/10.0)),(p/10.0)])
        avg.append(sum(list)*10/t)
    return avg


'''
Description: Creates and outputs graphs
Params: avg, b
Output: histogram, dotplot
'''
def qualgraph(avg, b):
    b = b*10

    '''histogram'''
    bx = plt.figure()
    bx = sns.distplot(pd.Series(avg,name="Self-Rating"))
    
    
    '''dotplot :('''
    #number of bins
    bins = np.arange((100.0/b)+2)*b/10
    
    #figure scaling, axis labels, and ticks
    p = plt.figure(figsize=(10,20))
    ax = plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(b/5))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(b/10))
    p.add_axes(ax)
    p.suptitle('Distribution of Averages', fontsize=20)
    plt.xlabel('Average', fontsize=18)
    plt.ylabel('Frequency', fontsize=18)
    
    #set up and set frequency and value tables
    hist, edges = np.histogram(avg,bins=bins,)#range=(0,10))
    y = np.arange(1,hist.max()+1)
    x = np.arange((100.0/b)+1)/(10.0/b)
    X,Y = np.meshgrid(x,y)
    
    #plot the points
    plt.scatter(X,Y, c=Y<=hist, cmap="Greys",s=1)
    
    #save the figure to dot.png
    #p.savefig("dot")
    return bx, p
 
    
'''
Description: Calculates statistical data
Params: values, avg
Output: mean, standard deviance, if & why normally distributed
'''
def stats(n, avg):
    #mean
    list = []
    m = sum(avg)/n
    
    #StDev
    for i in range(len(avg)):
        list.append(avg[i] - m)
    #print(avg)
    s = math.sqrt(sum(avg)/(n-1))
    
    return m,s


'''
Program to run when file is not imported
Same as web version
'''
if __name__ == '__main__':
    
    # Initialize values
    values = initialize()
    
    #Command line arguments
    if(len(sys.argv)):
        for i in range(1,len(sys.argv)):
            #Probability
            if sys.argv[i][0]=='p':
                values[0] = float(sys.argv[i][2:])
            #Number of Trials
            elif sys.argv[i][0]=='n':
                values[1] = int(sys.argv[i][2:])
            #Size of bins
            elif sys.argv[i][0]=='b':
                values[2] = float(sys.argv[i][2:])
            #Size of trials
            elif sys.argv[i][0]=='t':
                values[3] = int(sys.argv[i][2:])
            #Seed for trial generation
            elif sys.argv[i][0]=='s':
                s = int(sys.argv[i][2:])
                np.random.seed(s)
            #Flag for official runs
            elif sys.argv[i]=='-w':
                w = 1
            #error if not any of these
            else:
                raise ValueError(sys.argv[i],' is not a valid argument.')

    #Take sample
    avg = sample(values[0],values[1],values[3])
    #print(avg)

    #Create graphs
    hist, dot = qualgraph(avg, values[2])
    #print(hist, dot)
    
    #Create statistics
    m, s = stats(values[1], avg)
    #print("mean: " + m + "\nStandard Dev: " + s)
    
    #Output important shit
    print("{}\n{}\n\nMean: {}\nStandard Dev: {}".format(values,avg,m,s))