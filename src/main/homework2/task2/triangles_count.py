from scipy.sparse import tril, csr_matrix


"""
IN:
    m -- adjacency matrix as list of lists.
OUT:
    c -- count of triangles.
"""


def triangles_count(m):
    def compute():
        triangle_matrix = tril(matrix)

        return int(triangle_matrix.multiply(triangle_matrix * triangle_matrix).sum())

    matrix = csr_matrix(m)

    return compute()
