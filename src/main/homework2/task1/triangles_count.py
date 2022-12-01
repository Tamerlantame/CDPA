from pygraphblas import Matrix


"""
IN: 
    m -- information about each edge as list of 3 lists. 
    1st -- info about sources, 2nd -- info about targets, 3rd -- info about weights (only units allowed).
OUT:
    c -- count of triangles.
"""


def triangles_count(m):
    def compute():
        triangle_matrix = matrix.tril()

        return triangle_matrix.mxm(triangle_matrix, mask=triangle_matrix).reduce_int()

    matrix = Matrix.from_lists(m[0], m[1], m[2])

    return compute()
