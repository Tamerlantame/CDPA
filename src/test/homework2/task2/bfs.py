import unittest
from src.main.homework2.task2.bfs import bfs


class Bfs(unittest.TestCase):
    def test_bfs_with_acyclic_graph(self):
        matrix_info = [[0, 0, 1, 1, 5],
                       [1, 4, 3, 5, 2],
                       [1, 1, 2, 4, 1]]
        start = 0

        expect = [1, 2, 4, 3, 2, 3]
        result = bfs(matrix_info, start).to_lists()[1]

        self.assertListEqual(expect, result)

    def test_bfs_with_cyclic_graph(self):
        matrix_info = [[0, 0, 1, 1, 5, 1, 4],
                       [1, 4, 3, 5, 2, 0, 1],
                       [7, 7, 1, 12, 1, 1, 1]]
        start = 0

        expect = [1, 2, 4, 3, 2, 3]
        result = bfs(matrix_info, start).to_lists()[1]

        self.assertListEqual(expect, result)

    def test_bfs_with_graph_with_loops(self):
        matrix_info = [[0, 0, 1, 1, 5, 4],
                       [1, 4, 3, 5, 2, 4],
                       [1, 1, 1, 3, 1, 1]]
        start = 0

        expect = [1, 2, 4, 3, 2, 3]
        result = bfs(matrix_info, start).to_lists()[1]

        self.assertListEqual(expect, result)