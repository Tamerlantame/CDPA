import unittest
import numpy as np
from src.main.homework2.task2.sssp import sssp


class Sssp(unittest.TestCase):
    def test_sssp_with_acyclic_graph(self):
        matrix = [[0, 5, 0, 0, 0, 3],
                  [0, 0, 0, 2, 7, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0]]
        start = 0

        expect = [0, 5, 13, 7, 12, 3]
        result = sssp(matrix, start)

        self.assertTrue(np.array_equal(expect, result))

    def test_sssp_with_cyclic_graph(self):
        matrix = [[0, 5, 0, 0, 0, 3],
                  [3, 0, 0, 2, 7, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0],
                  [0, 2, 0, 0, 0, 0]]
        start = 0

        expect = [0, 5, 13, 7, 12, 3]
        result = sssp(matrix, start)

        self.assertTrue(np.array_equal(expect, result))

    def test_sssp_with_2_paths_to_1_node(self):
        matrix = [[0, 5, 0, 0, 0, 3],
                  [0, 0, 0, 2, 7, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0],
                  [0, 0, 10, 0, 0, 0]]
        start = 0

        expect = [0, 5, 13, 7, 12, 3]
        result = sssp(matrix, start)

        self.assertTrue(np.array_equal(expect, result))
