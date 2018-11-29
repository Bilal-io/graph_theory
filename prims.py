from  Weighted_Graph import Weighted_Graph
from functions import min_incident_edge, update


def prims(edge_file_name, start_vertex = 0, draw = False):
    T = ({start_vertex},[])
    G = Weighted_Graph(edge_file_name)
    while T[0] != G.vertex_set():
        update(T,G)
    if draw == True:
        G.draw_graph()
    return COST