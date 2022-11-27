import unittest
from src.main.homework2.task2.triangles_count import triangles_count


class TrianglesCount(unittest.TestCase):
    def test_triangles_count_with_graph_without_triangle(self):
        matrix = [[0, 1, 1, 0, 0],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 1, 1],
                  [0, 0, 1, 0, 0],
                  [0, 0, 1, 0, 0]]

        expect = 0
        result = triangles_count(matrix)

        self.assertEqual(expect, result)

    def test_triangles_count_with_triangles(self):
        matrix = [[0, 1, 1, 0, 0],
                  [1, 0, 1, 0, 0],
                  [1, 1, 0, 1, 1],
                  [0, 0, 1, 0, 1],
                  [0, 0, 1, 1, 0]]

        expect = 2
        result = triangles_count(matrix)

        self.assertEqual(expect, result)

    def test_triangles_count_with_two_general_nodes_for_triangles(self):
        matrix = [[0, 1, 1, 1, 1],
                  [1, 0, 1, 1, 1],
                  [1, 1, 0, 0, 0],
                  [1, 1, 0, 0, 0],
                  [1, 1, 0, 0, 0]]

        expect = 3
        result = triangles_count(matrix)

        self.assertEqual(expect, result)
