import Weighted_Graph



#
from Weighted_Graph import *
G = Weighted_Graph('test_graph.txt')
G.draw_graph()
#print(G.edge_set())
#print(G.vertex_set())
#print(G.edge_dict())
#H = ({0,1,3},[(0,1),(1,3)])
#print(G.draw_subgraph(H))
#



def C(e,G):
    return G.edge_dict()[e]

#check function
#print(C((1,4),G))

T = ({2,3},[(2,3)])
#    {end points}, [edges] 

# not finsiehd, get rid of any end points that exists in T
def incident_edges(T,G):
    edges = []
    for v in T[0]:
        for e in G.edge_set():
            if v in e:
                edges.append(e)
    for e in edges:
        if e in T[1]:
            edges.remove(e)
    return edges

# finish
def min_incident_edge(T,G):
    edges = incident_edges(T,G)
    min_edge = edges[0]
    for e in edges:
        #if... get min weight
        return 0 # remove this
    return min_edge

# update T
def update(T,G):
    return 0