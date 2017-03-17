from random import choice

def get_edges(filename):
    """
    a method that take a file name, format (nodeID edge1 edge2 edge3 ....)
    and a list of  tuples[(node1, node2), ....] representing the edges
    """
    f = open(filename)
    edges = []
    for line in f:
        tmp = line.strip().split()
        if len(tmp) < 1:
            continue
        for i in range(1, len(tmp)):
            tmp_edge = (tmp[0], tmp[i])
            edges.append(tmp_edge)
    return edges

def get_minCut(edges):

    while len(set(edges)) > 2:
        current_edge = choice(edges)
        edges.remove(current_edge)
        #iterate over edges and change current_edge[1] to current_edge[0]
        edges = map(lambda x: (current_edge[0] if x[0] == current_edge[1] else x[0], current_edge[0] if x[1] == current_edge[1] else x[1]), edges)
        #remove self loops
        edges = filter(lambda x: x[0] != x[1], edges)

    edges = filter(lambda x: x[0] < x[1], edges)
    return len(edges)

tmp = 1000
filename = "KargerMinCut.txt"
edges = get_edges(filename)
for i in range(300):
    x = get_minCut(list(edges))
    if x < tmp:
        tmp = x
print tmp
