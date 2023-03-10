    # Python program for Dijkstra's single
    # source shortest path algorithm. The program is
    # for adjacency matrix representation of the graph
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np
def dijikstraalgo(filename):    # Library for INT_MAX
    max=999999
    vertex=[]
    class Graph():
    
        def __init__(self, vertices):
            self.V = vertices
            self.graph = [[0 for column in range(vertices)]
                        for row in range(vertices)]
    
        def printSolution(self, dist):
            print ("Vertex \tDistance from Source")
            for node in range(self.V):
                print (node, "\t", format(dist[node],'.2f'))
                vertex.append(format(dist[node],'.2f'))

            
    

        # A utility function to find the vertex with
        # minimum distance value, from the set of vertices
        # not yet included in shortest path tree
        def minDistance(self, dist, sptSet):
    
            # Initialize minimum distance for next node
            min = max
    
            # Search not nearest vertex not in the
            # shortest path tree
            for u in range(self.V):
                if dist[u] < min and sptSet[u] == False:
                    min = dist[u]
                    min_index = u
            return min_index
    
        # Function that implements Dijkstra's single source
        # shortest path algorithm for a graph represented
        # using adjacency matrix representation
        def dijkstra(self, src):
    
            dist = [max] * self.V
            dist[src] = 0
            sptSet = [False] * self.V
    
            for cout in range(self.V):
    
                # Pick the minimum distance vertex from
                # the set of vertices not yet processed.
                # x is always equal to src in first iteration
                x = self.minDistance(dist, sptSet)
    
                # Put the minimum distance vertex in the
                # shortest path tree
                sptSet[x] = True
    
                # Update dist value of the adjacent vertices
                # of the picked vertex only if the current
                # distance is greater than new distance and
                # the vertex in not in the shortest path tree
                for y in range(self.V):
                    if self.graph[x][y] > 0 and sptSet[y] == False and \
                    dist[y] > dist[x] + self.graph[x][y]:
                            dist[y] = dist[x] + self.graph[x][y]
    
            self.printSolution(dist)
    
    with open(filename+'.txt') as f:
        flat_list=[word for line in f for word in line.split()]
    total_nodes=int(flat_list[0])
    starting_node=int(flat_list[1])
    i=2
    g=Graph(total_nodes)
    G = np.zeros(( total_nodes, total_nodes) )
    while(i<len(flat_list)):
        g.graph[int(flat_list[i])][int(flat_list[i+1])]=int(flat_list[i+2])/10000000
        i=i+3
    # INF = 9999999
    for i in range(total_nodes):
        for j in range(total_nodes):
            if(g.graph[i][j]==0):
                g.graph[i][j]=g.graph[j][i]

    #print(g.graph) 
    g.dijkstra(starting_node);
    print("\n")
    G=nx.Graph()
    for i in range(total_nodes-1):
        for j in range(total_nodes-1):
            if(g.graph[i][j]!=0): 
                G.add_edges_from([(i,j)],weight=g.graph[i][j])
    pos=nx.spring_layout(G)
    _labels=dict([((u,v,),d['weight'])
                    for u,v,d in G.edges(data=True)])
    labeldict = {}
    #vertex=[0,4,12,19,21,11,9,8,14]
    #print(vertex)
    for i in range(total_nodes-1):
        labeldict[i] = 'N='+str(i) +'d='+ str(vertex[i]) 
    nx.draw(G, labels = labeldict, with_labels = True ,node_size=3500)
    plt.show()
#dijikstraalgo()