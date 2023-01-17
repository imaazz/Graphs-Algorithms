    # Prim's Algorithm in Python
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np
def primsalgo(filename):
    #Filing 
    with open(filename+'.txt') as f:
        flat_list=[word for line in f for word in line.split()]
    total_nodes=int(flat_list[0])
    G = np.zeros(( total_nodes, total_nodes) )
    starting_node=int(flat_list[1])
    print(starting_node)
    i=2
    while(i<len(flat_list)):
        G[int(flat_list[i])][int(flat_list[i+1])]=int(flat_list[i+2])/10000000
        i=i+3
    INF = 9999999
    for i in range(total_nodes):
        for j in range(total_nodes):
            if(G[i][j]==0):
                G[i][j]=G[j][i]
            if(G[i][j]>G[j][i] and G[i][j] and G[j][i]):
               G[i][j]=G[j][i]             
    #print(G)
    #Prims Algo
    selected_node=np.zeros(total_nodes)
    no_edge = 0
    vertex1=[]
    vertex2=[]
    vertex3=[]
    selected_node[0] = True
    min_cost=0
    # printing for edge and weight
    print("Edge : Weight\n")
    while (no_edge < total_nodes - 1):
        
        minimum = INF
        a = 0
        b = 0
        for m in range(total_nodes):
            if selected_node[m]:
                for n in range(total_nodes):
                    if ((not selected_node[n]) and G[m][n]):  
                        # not in selected and there is an edge
                        if minimum > G[m][n]:
                            minimum = G[m][n]
                            a = m
                            b = n
        print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
        vertex1.append(str(a))
        vertex2.append(str(b))
        vertex3.append(format(float(str(G[a][b])),'.2f'))
        selected_node[b] = True
        no_edge += 1
        min_cost+=float(str(G[a][b]))
    print("Minimum cost= {}".format(min_cost))
    #Plotting Graph
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
#primsalgo("input10")