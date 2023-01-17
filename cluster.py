import itertools
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np
def clusteralgo(filename):
    def l(a,i,r):
        s=[b for b in r if a[i][b]]
        k=len(s)
        if k<2:
            return 0
        return 2.0*sum(map(lambda x:a[x[0]][x[1]],itertools.combinations(s,2)))/k/(k-1)
    def g(a):
        n=len(a)
        r=range(n)
        return sum([l(a,i,r) for i in r])/n
    #print(g([[1,1,1],[1,1,1],[1,1,1]]))
    with open(filename+'.txt') as f:
        flat_list=[word for line in f for word in line.split()]
    total_nodes=int(flat_list[0])
    G = np.zeros(( total_nodes, total_nodes) )
    starting_node=int(flat_list[1])
    i=2
    while(i<len(flat_list)-1):
        G[int(flat_list[i])][int(flat_list[i+1])]=int(flat_list[i+2])/10000000
        i=i+3
    INF = 9999999
    for i in range(total_nodes):
        for j in range(total_nodes):
            if(G[i][j]==0):
                G[i][j]=G[j][i]
            if(G[i][j]>G[j][i] and G[i][j] and G[j][i]):
                G[i][j]=G[j][i]
    print("Clustering Coefficent is ",g(G))             