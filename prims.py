from Weighted_Graph import Weighted_Graph
from functions import min_incident_edge, update, C, incident_edges


def prims(edge_file_name, start_vertex, draw=False):
    T = ({start_vertex}, [])
    G = Weighted_Graph(edge_file_name)
    cost = 0
    while T[0] != G.vertex_set():
        update(T, G)
    if draw == True:

        G.draw_subgraph(T)
    for e in T[1]:
        cost += G.edge_dict()[e]
    return cost
