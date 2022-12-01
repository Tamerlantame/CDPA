from pygraphblas import Matrix, Vector, INT64


"""
IN: 
    m -- information about each edge as list of 3 lists. 
    1st -- info about sources, 2nd -- info about targets, 3rd -- info about weights.

    start -- start vertex index.
OUT:
    v -- Vector, which contains shortest path length from start to vertex with number n at position with number n.
"""


def sssp(m, start):
    def compute():
        result = Vector.sparse(matrix.type, matrix.nrows)
        result[start] = 0

        for i in range(matrix.nrows-1):
            result.min_plus(matrix, out=result, accum=INT64.min)
            if result == matrix:
                break
        return result

    matrix = Matrix.from_lists(m[0], m[1], m[2])

    return compute()
