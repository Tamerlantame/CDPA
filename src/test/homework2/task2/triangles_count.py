import unittest
from src.main.homework2.task2.triangles_count import triangles_count


class TriangleCount(unittest.TestCase):
    def test_triangle_count_with_graph_without_triangle(self):
        matrix_info = [[0, 0, 1, 2, 2, 2, 3, 4],
                       [1, 2, 0, 0, 3, 4, 2, 2],
                       [1, 1, 1, 1, 1, 1, 1, 1]]

        expect = 0
        result = triangles_count(matrix_info)

        self.assertEqual(expect, result)

    def test_triangle_count_with_triangles(self):
        matrix_info = [[0, 0, 1, 2, 2, 2, 3, 4, 1, 2, 3, 4],
                       [1, 2, 0, 0, 3, 4, 2, 2, 2, 1, 4, 3],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        expect = 2
        result = triangles_count(matrix_info)

        self.assertEqual(expect, result)

    def test_triangle_count_with_two_general_nodes_for_triangles(self):
        matrix_info = [[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4],
                       [1, 2, 3, 4, 0, 2, 3, 4, 0, 1, 0, 1, 0, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        expect = 3
        result = triangles_count(matrix_info)

        self.assertEqual(expect, result)