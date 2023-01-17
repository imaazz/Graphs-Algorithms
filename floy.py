    # Number of vertices

    # for adjacency matrix representation of the graph
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np
def floydalgo(filename):
    INF = 99999
    with open(filename+'.txt') as f:
        flat_list=[word for line in f for word in line.split()]
    total_nodes=int(flat_list[0])
    starting_node=int(flat_list[1])
    i=2
    G = np.zeros(( total_nodes, total_nodes) )
    while(i<len(flat_list)-1):
        G[int(flat_list[i])][int(flat_list[i+1])]=int(flat_list[i+2])/10000000
        i=i+3
    # INF = 9999999
    for i in range(total_nodes):
        for j in range(total_nodes):
            if(G[i][j]==0):
                G[i][j]=G[j][i]
                if(G[i][j]==0 and i!=j):
                    G[i][j]=INF
    # Algorithm 
    def floyd():
        dist = list(map(lambda p: list(map(lambda q: q, p)), G))

        # Adding vertices individually
        for r in range(total_nodes):
            for p in range(total_nodes):
                for q in range(total_nodes):
                    dist[p][q] = min(dist[p][q], dist[p][r] + dist[r][q])
        sol(dist)

    # Printing the output
    def sol(dist):
        for p in range(total_nodes):
            for q in range(total_nodes):
                if(dist[p][q] == INF):
                    print("INF", end=" ")
                else:
                    print(format(dist[p][q],'.2f'), end="  ")
            print(" ")
    floyd()
#floydalgo()