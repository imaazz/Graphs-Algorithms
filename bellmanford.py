import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np
def bellmanfordalgo(filename):
    vertex=[]
    vertex1=[]
    vertex2=[]
    vertex3=[]
    # Python3 program for Bellman-Ford's single source
    # shortest path algorithm.
    
    # Class to represent a graph
    class Graph:
    
        def __init__(self, vertices):
            self.V = vertices # No. of vertices
            self.graph = []
    
        # function to add an edge to graph
        def addEdge(self, u, v, w):
            self.graph.append([u, v, w])
            
        # utility function used to print the solution
        def printArr(self, dist):
            print("Vertex Distance from Source")
            for i in range(self.V):
                print("{0}\t\t{1}".format(i, dist[i]))
                vertex.append(format(dist[i],'.2f'))
        
        # The main function that finds shortest distances from src to
        # all other vertices using Bellman-Ford algorithm. The function
        # also detects negative weight cycle
        def BellmanFord(self, src):
    
            # Step 1: Initialize distances from src to all other vertices
            # as INFINITE
            dist = [float("Inf")] * self.V
            dist[src] = 0
    
    
            # Step 2: Relax all edges |V| - 1 times. A simple shortest
            # path from src to any other vertex can have at-most |V| - 1
            # edges
            for _ in range(self.V - 1):
                # Update dist value and parent index of the adjacent vertices of
                # the picked vertex. Consider only those vertices which are still in
                # queue
                for u, v, w in self.graph:
                    if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                            dist[v] = dist[u] + w
    
            # Step 3: check for negative-weight cycles. The above step
            # guarantees shortest distances if graph doesn't contain
            # negative weight cycle. If we get a shorter path, then there
            # is a cycle.
    
            for u, v, w in self.graph:
                    if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                            print("Graph contains negative weight cycle")
                            return
                            
            # print all distance
            self.printArr(dist)
    INF = 99999999
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
    g = Graph(total_nodes)
    for i in range (total_nodes):
        for j in range(total_nodes):
            g.addEdge(i, j, G[i][j])
            vertex1.append(i)
            vertex2.append(j)
            vertex3.append(format(G[i][j],'.2f'))
    g.BellmanFord(starting_node)
    #print(G)
   # print(vertex)
    print("\n")
    G=nx.Graph()
    for i in range(len(vertex1)):
        #for j in range(total_nodes-1):
        if(vertex3[i]!=0 and vertex3[i]!=INF): 
            G.add_edges_from([(vertex1[i],vertex2[i])],weight=vertex3[i])
    pos=nx.spring_layout(G)
    _labels=dict([((u,v,),d['weight'])
                    for u,v,d in G.edges(data=True)])
    labeldict = {}
        #vertex=[0,4,12,19,21,11,9,8,14]
    #print(vertex)
    for i in range(total_nodes):
        labeldict[i] = 'N='+str(i) +'d='+ str(vertex[i]) 
    nx.draw(G, labels = labeldict, with_labels = True ,node_size=3500)
    plt.show()