import unittest
import numpy as np
from src.main.homework2.task1.bfs import bfs


class Bfs(unittest.TestCase):
    def test_bfs_with_acyclic_graph(self):
        matrix = [[0, 5, 0, 0, 0, 3],
                  [0, 0, 0, 2, 7, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0]]
        start = 0

        expect = [0, 1, 5, 3, 4, 2]
        result = bfs(matrix, start)

        self.assertTrue(np.array_equal(expect, result))

    def test_bfs_with_cyclic_graph(self):
        matrix = [[0, 5, 0, 0, 0, 3],
                  [3, 0, 0, 2, 7, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0],
                  [0, 2, 0, 0, 0, 0]]
        start = 0

        expect = [0, 1, 5, 3, 4, 2]
        result = bfs(matrix, start)

        self.assertTrue(np.array_equal(expect, result))

    def test_bfs_with_graph_with_loops(self):
        matrix = [[1, 5, 0, 0, 0, 3],
                  [0, 0, 0, 2, 7, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 4, 0, 0],
                  [0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0]]
        start = 0

        expect = [0, 1, 5, 3, 4, 2]
        result = bfs(matrix, start)

        self.assertTrue(np.array_equal(expect, result))
