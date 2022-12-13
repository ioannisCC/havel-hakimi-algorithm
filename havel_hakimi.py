from email.policy import default
from random import randint
import networkx as nx
import matplotlib.pyplot as plt

g_nodes = int(input("Give number of graph nodes: "))
while(g_nodes < 0):
    g_nodes = int(input("Please enter valid number of nodes"))

nodes_degree = []
for i in range(g_nodes):
    node_degree = int(input("Give the degree if the node " + str(i+1) + ": "))
    while (node_degree < 0):
        node_degree = int(input("Please enter valid degree of the node " + str(i+1) + ": "))
    nodes_degree.append(node_degree)

if nx.is_graphical(nodes_degree):
    Ve = []
    for i in range(g_nodes):
        Ve.append(i+1)

    Ed = []
    E_temp = []
    for i in range(len(nodes_degree)):
        node = randint(0,len(nodes_degree) - 1)
        degree = nodes_degree[node]
        nodes_degree.pop(node)
        for j in range(degree):
            max_degree = max(nodes_degree, default=0)
            E_temp.append(node)
            E_temp.append(max_degree)
        for k in range(len(nodes_degree) - 1):
            nodes_degree[k] = nodes_degree[k] - 1
    for x in range(0,len(E_temp) - 1,2):
        Ed.append(E_temp[x:x+2])

    G = nx.Graph()
    G.add_nodes_from(Ve)
    G.add_edges_from(Ed)

    nx.draw_networkx(G) #Draw the graph G
    plt.savefig("graph.eps") #Save the drawing of G
    plt.show() #Show the drawing of G on screen
else :
    print ("The sequence ",nodes_degree ,"is not graphical, so a ghraph can't be made with Havel-Hakimi algorithm")
    print ("")




    
        


