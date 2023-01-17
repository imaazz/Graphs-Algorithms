
    # Boruvka's algorithm to find Minimum Spanning
    # Tree of a given connected, undirected and weighted graph
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np
from collections import defaultdict
def boruvkasalgo(filename):   
    #Class to represent a graph
    class Graph:
    
        def __init__(self,vertices):
            self.V= vertices #No. of vertices
            self.graph = [] # default dictionary to store graph

        def _plotting(self,vertex1,vertex2,vertex3):
            G=nx.Graph()
            for i in range(total_nodes-1): 
                G.add_edges_from([(vertex1[i],vertex2[i])],weight=vertex3[i])
            pos=nx.spring_layout(G)
            _labels=dict([((u,v,),d['weight'])
                            for u,v,d in G.edges(data=True)])
            nx.draw_networkx_nodes(G,pos,node_size=500)
            nx.draw_networkx_edges(G,pos,edgelist=G.edges(),edge_color='black')
            nx.draw_networkx_edge_labels(G,pos,edge_labels=_labels)
            nx.draw_networkx_labels(G,pos)
            plt.show()      
    
        # function to add an edge to graph
        def addEdge(self,u,v,w):
            self.graph.append([u,v,w])
    
        # A utility function to find set of an element i
        # (uses path compression technique)
        def find(self, parent, i):
            if parent[i] == i:
                return i
            return self.find(parent, parent[i])
    
        # A function that does union of two sets of x and y
        # (uses union by rank)
        def union(self, parent, rank, x, y):
            xroot = self.find(parent, x)
            yroot = self.find(parent, y)
    
            # Attach smaller rank tree under root of high rank tree
            # (Union by Rank)
            if rank[xroot] < rank[yroot]:
                parent[xroot] = yroot
            elif rank[xroot] > rank[yroot]:
                parent[yroot] = xroot
            #If ranks are same, then make one as root and increment
            # its rank by one
            else :
                parent[yroot] = xroot
                rank[xroot] += 1
    
        # The main function to construct MST using Kruskal's algorithm
        def boruvkaMST(self):
            parent = []; rank = []; 
            vertex1=[]
            vertex2=[]
            vertex3=[]
            # An array to store index of the cheapest edge of
            # subset. It store [u,v,w] for each component
            cheapest =[]
    
            # Initially there are V different trees.
            # Finally there will be one tree that will be MST
            numTrees = self.V
            MSTweight = 0
    
            # Create V subsets with single elements
            for node in range(self.V):
                parent.append(node)
                rank.append(0)
                cheapest =[-1] * self.V
        
            # Keep combining components (or sets) until all
            # compnentes are not combined into single MST
    
            while numTrees > 1:
    
                # Traverse through all edges and update
                # cheapest of every component
                for i in range(len(self.graph)):
    
                    # Find components (or sets) of two corners
                    # of current edge
                    u,v,w =  self.graph[i]
                    set1 = self.find(parent, u)
                    set2 = self.find(parent ,v)
    
                    # If two corners of current edge belong to
                    # same set, ignore current edge. Else check if 
                    # current edge is closer to previous
                    # cheapest edges of set1 and set2
                    if set1 != set2:     
                        
                        if cheapest[set1] == -1 or cheapest[set1][2] > w :
                            cheapest[set1] = [u,v,w] 
    
                        if cheapest[set2] == -1 or cheapest[set2][2] > w :
                            cheapest[set2] = [u,v,w]
    
                # Consider the above picked cheapest edges and add them
                # to MST
                for node in range(self.V):
    
                    #Check if cheapest for current set exists
                    if cheapest[node] != -1:
                        u,v,w = cheapest[node]
                        set1 = self.find(parent, u)
                        set2 = self.find(parent ,v)
    
                        if set1 != set2 :
                            MSTweight += w
                            self.union(parent, rank, set1, set2)
                            print ("Edge %d-%d with weight %d included in MST" % (u,v,w))
                            vertex1.append(u)
                            vertex2.append(v)
                            vertex3.append(format(w,'.2f'))
                            numTrees = numTrees - 1
                
                #reset cheapest array
                cheapest =[-1] * self.V
    
                
            print ("Weight of MST is %d" % MSTweight)
            g._plotting(vertex1,vertex2,vertex3)
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
    g = Graph(total_nodes)
    for i in range(total_nodes):
        for j in range(total_nodes):
            g.addEdge(i, j, G[i][j])


    g.boruvkaMST()
#boruvkasalgo()                       