from igraph import Graph


"""
IN:
    m -- adjacency matrix as list of lists.
OUT:
    c -- count of triangles.
"""


def triangles_count(m):
    def compute():
        return len(matrix.cliques(3, 3))

    matrix = Graph.Adjacency(m)

    return compute()
