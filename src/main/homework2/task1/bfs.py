from pygraphblas import Matrix, Vector, UINT8, BOOL, descriptor


"""
IN: 
    m -- information about each edge as list of 3 lists. 
    1st -- info about sources, 2nd -- info about targets, 3rd -- info about weights.
    
    start -- start vertex index.
OUT:
    v -- Vector, which contains level of vertex with number n at position with number n.
"""


def bfs(m, start):
    def compute():
        result = Vector.sparse(UINT8, matrix.nrows)
        current = Vector.sparse(BOOL, matrix.nrows)
        current[start] = True

        for level in range(1, matrix.nrows + 1):
            if not current.reduce_bool():
                break
            result.assign_scalar(level, mask=current)
            result.vxm(matrix, mask=result, out=current, desc=descriptor.RC)

        return result

    matrix = Matrix.from_lists(m[0], m[1], m[2])

    return compute()

