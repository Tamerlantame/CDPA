import random
import unittest
import numpy as np
from src.main.homework2.task1.bfs import bfs as pygraphblas_bfs
from src.main.homework2.task2.bfs import bfs as scipy_bfs
from src.main.homework2.task3.bfs import bfs as igraph_bfs

from src.main.homework2.task1.sssp import sssp as pygraphblas_sssp
from src.main.homework2.task2.sssp import sssp as scipy_sssp
from src.main.homework2.task3.sssp import sssp as igraph_sssp

from src.main.homework2.task1.triangles_count import triangles_count as pygraphblas_triangles_count
from src.main.homework2.task2.triangles_count import triangles_count as scipy_triangles_count
from src.main.homework2.task3.triangles_count import triangles_count as igraph_triangles_count


def results_are_equal_on_random_graph(n, scipy_f, igraph_f, triangles):
    vertices = range(n)

    if triangles:
        matrix = [[0] * n] * n
        for i in vertices:
            for j in vertices:
                if bool(random.getrandbits(1)):
                    matrix[i][j] = 1
                    matrix[j][i] = 1

        result = np.array_equal(scipy_f(matrix), igraph_f(matrix))
    else:
        matrix = list(map(lambda i: list(map(lambda j: random.randint(0, 10), vertices)), vertices))

        result = np.array_equal(scipy_f(matrix, 0), igraph_f(matrix, 0))

    return result


def results_are_equal(matrix, grb_matrix_info, pygraphblas_f, scipy_f, igraph_f, triangles):
    if triangles:
        grb_result = pygraphblas_f(grb_matrix_info)
        scipy_result = scipy_f(matrix)
        igraph_result = igraph_f(matrix)

        result = grb_result == scipy_result == igraph_result
    else:
        grb_result = pygraphblas_f(grb_matrix_info, 0).to_lists()[1]
        scipy_result = scipy_f(matrix, 0)
        igraph_result = igraph_f(matrix, 0)

        result = np.array_equal(np.array(grb_result), scipy_result) and np.array_equal(scipy_result, igraph_result)

    return result


class Common(unittest.TestCase):
    def test_scipy_and_igraph_bfs_with_random_graphs(self):
        map(lambda i: self.assertTrue(results_are_equal_on_random_graph(i + 1, scipy_bfs, igraph_bfs, False)),
            range(100))

    def test_scipy_and_igraph_sssp_with_random_graphs(self):
        map(lambda i: self.assertTrue(results_are_equal_on_random_graph(i + 1, scipy_sssp, igraph_sssp, False)),
            range(100))

    def test_sssp_with_acyclic_graph(self):
        matrix = [[0, 3, 0, 0, 7, 0],
                  [0, 0, 0, 2, 0, 4],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0]]
        grb_matrix_info = [[0, 0, 1, 1, 5],
                           [1, 4, 3, 5, 2],
                           [3, 7, 2, 4, 1]]

        self.assertTrue(results_are_equal(matrix, grb_matrix_info, pygraphblas_sssp, scipy_sssp, igraph_sssp, False))

    def test_sssp_with_cyclic_graph(self):
        matrix = [[0, 3, 0, 0, 7, 0],
                  [1, 0, 0, 2, 0, 4],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 7, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0]]
        grb_matrix_info = [[0, 0, 1, 1, 5, 1, 4],
                           [1, 4, 3, 5, 2, 0, 1],
                           [3, 7, 2, 4, 1, 1, 7]]

        self.assertTrue(results_are_equal(matrix, grb_matrix_info, pygraphblas_sssp, scipy_sssp, igraph_sssp, False))

    def test_sssp_with_2_paths_to_1_node(self):
        matrix = [[0, 3, 0, 0, 7, 0],
                  [1, 0, 0, 2, 0, 4],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 2, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0]]
        grb_matrix_info = [[0, 0, 1, 1, 4, 5],
                           [1, 4, 3, 5, 2, 2],
                           [3, 7, 2, 4, 2, 1]]

        self.assertTrue(results_are_equal(matrix, grb_matrix_info, pygraphblas_sssp, scipy_sssp, igraph_sssp, False))

    def test_scipy_and_igraph_triangles_count_with_random_graphs(self):
        map(lambda i: self.assertTrue(results_are_equal_on_random_graph(i + 1, scipy_triangles_count,
                                                                        igraph_triangles_count, True)),
            range(100))

    def test_triangle_count_with_graph_without_triangle(self):
        matrix = [[0, 1, 1, 0, 0],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 1, 1],
                  [0, 0, 1, 0, 0],
                  [0, 0, 1, 0, 0]]
        grb_matrix_info = [[0, 0, 1, 2, 2, 2, 3, 4],
                           [1, 2, 0, 0, 3, 4, 2, 2],
                           [1, 1, 1, 1, 1, 1, 1, 1]]

        self.assertTrue(results_are_equal(matrix, grb_matrix_info, pygraphblas_triangles_count,
                                          scipy_triangles_count, igraph_triangles_count, True))

    def test_triangle_count_with_triangles(self):
        matrix = [[0, 1, 1, 0, 0],
                  [1, 0, 1, 0, 0],
                  [1, 1, 0, 1, 1],
                  [0, 0, 1, 0, 1],
                  [0, 0, 1, 1, 0]]
        grb_matrix_info = [[0, 0, 1, 2, 2, 2, 3, 4, 1, 2, 3, 4],
                           [1, 2, 0, 0, 3, 4, 2, 2, 2, 1, 4, 3],
                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        self.assertTrue(results_are_equal(matrix, grb_matrix_info, pygraphblas_triangles_count,
                                          scipy_triangles_count, igraph_triangles_count, True))

    def test_triangle_count_with_two_general_nodes_for_triangles(self):
        matrix = [[0, 1, 1, 1, 1],
                  [1, 0, 1, 1, 1],
                  [1, 1, 0, 0, 0],
                  [1, 1, 0, 0, 0],
                  [1, 1, 0, 0, 0]]
        grb_matrix_info = [[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4],
                           [1, 2, 3, 4, 0, 2, 3, 4, 0, 1, 0, 1, 0, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        self.assertTrue(results_are_equal(matrix, grb_matrix_info, pygraphblas_triangles_count,
                                          scipy_triangles_count, igraph_triangles_count, True))