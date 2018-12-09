from Weighted_Graph import Weighted_Graph


def C(e, G):
    return G.edge_dict()[e]


def incident_edges(T, G):
    edges = []
    for v in T[0]:
        for e in G.edge_set():
            if v in e and e not in edges:
                edges.append(e)

    # filter the edges
    edges = [e for e in edges if (e[0] not in T[0] or e[1] not in T[0])]

    return edges


def filter_incident_edges(T, G):
    edges = incident_edges(T, G)
    filtered_edges = [e for e in edges if (e[0] not in T[0] or e[1] not in T[0])]

    return filtered_edges


def min_incident_edge(T, G):
    edges = filter_incident_edges(T, G)
    min_edge = edges[0]
    for e in edges:
        if G.edge_dict()[min_edge] > G.edge_dict()[e]:
            min_edge = e
    return min_edge


def update(T, G):
    NewValues = min_incident_edge(T, G)
    for (
        i
    ) in (
        NewValues
    ):  # add both vertices in to T[0] only one will be added as the other already exists, but the order changes so that's a work-around.
        T[0].add(i)
    # if NewValues not in T[1]: # only add if not the new set does not exist already
    T[1].append(NewValues)
