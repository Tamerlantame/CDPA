from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import bellman_ford


"""
IN:
    m -- adjacency matrix as list of lists.
    start -- start vertex index.

OUT:
    a -- ndarray, which contains shortest path length from start to vertex with number n at position with number n.
"""


def sssp(m, start):
    def compute():
        return bellman_ford(csgraph=matrix, directed=True, indices=start, return_predecessors=False)

    matrix = csr_matrix(m)

    return compute()
