from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import breadth_first_order


"""
IN:
    m -- adjacency matrix as list of lists.
    start -- start vertex index.
    
OUT:
    a -- ndarray, which contains number in order of visit of vertex with index n at position with number n.
"""


def bfs(m, start):
    def compute():
        return breadth_first_order(matrix, start, directed=True)[0]

    matrix = csr_matrix(m)

    return compute()
