    # Python implementation for Kruskal's
    # algorithm
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np
def Kurskulalgo(filename):   # Find set of vertex i
    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i
    
    # Does union of i and j. It returns
    # false if i and j are already in same
    # set.
    def union(i, j):
        a = find(i)
        b = find(j)
        parent[a] = b
    
    # Finds MST using Kruskal's algorithm
    def kruskalMST(cost):
        mincost = 0 # Cost of min MST
        vertex1=[]
        vertex2=[]
        vertex3=[]   
    
        # Initialize sets of disjoint sets
        for i in range(V):
            parent[i] = i
    
        # Include minimum weight edges one by one
        edge_count = 0
        while edge_count < V - 1:
            min = INF
            a = -1
            b = -1
            for i in range(V):
                for j in range(V):
                    if find(i) != find(j) and cost[i][j] < min:
                        min = cost[i][j]
                        a = i
                        b = j
            union(a, b)
            print('Edge {}:({}, {}) cost:{}'.format(edge_count, a, b, min))
            vertex1.append(a)
            vertex2.append(b)
            vertex3.append(format(min,'.2f'))
            edge_count += 1
            mincost += min
    
        print("Minimum cost= {}".format(mincost))
        G=nx.Graph()
        for i in range(V-1): 
            G.add_edges_from([(vertex1[i],vertex2[i])],weight=vertex3[i])
        pos=nx.spring_layout(G)
        _labels=dict([((u,v,),d['weight'])
                        for u,v,d in G.edges(data=True)])
        nx.draw_networkx_nodes(G,pos,node_size=300)
        nx.draw_networkx_edges(G,pos,edgelist=G.edges(),edge_color='black')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=_labels)
        nx.draw_networkx_labels(G,pos)
        plt.show()
    

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
            if(G[i][j]==0):
                G[i][j]=INF

    #print(G)
    
    V = total_nodes
    parent = [i for i in range(V)]
    kruskalMST(G)
#Kurskulalgo()