from igraph import Graph


"""
IN:
    m -- adjacency matrix as list of lists.
    start -- start vertex index.
OUT:
    a -- list, which contains shortest path length from start to vertex with number n at position with number n.
"""


def sssp(m, start):
    def compute():
        return matrix.shortest_paths(start, weights=matrix.es["weight"])[0]

    matrix = Graph.Weighted_Adjacency(m)

    return compute()
