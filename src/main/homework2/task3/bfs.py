from igraph import Graph


"""
IN:
    m -- adjacency matrix as list of lists.
    start -- start vertex index.

OUT:
    a -- list, which contains number in order of visit of vertex with index n at position with number n.
"""


def bfs(m, start):
    def compute():
        return matrix.bfs(start)[0]

    matrix = Graph.Adjacency(m)

    return compute()
