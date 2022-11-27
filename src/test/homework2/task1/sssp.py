import unittest
from src.main.homework2.task1.sssp import sssp


class Sssp(unittest.TestCase):
    def test_sssp_with_acyclic_graph(self):
        matrix_info = [[0, 0, 1, 1, 5],
                       [1, 4, 3, 5, 2],
                       [3, 7, 2, 4, 1]]
        start = 0

        expect = [0, 3, 8, 5, 7, 7]
        result = sssp(matrix_info, start).to_lists()[1]

        self.assertListEqual(expect, result)

    def test_sssp_with_cyclic_graph(self):
        matrix_info = [[0, 0, 1, 1, 5, 1, 4],
                       [1, 4, 3, 5, 2, 0, 1],
                       [3, 7, 2, 4, 1, 1, 7]]
        start = 0

        expect = [0, 3, 8, 5, 7, 7]
        result = sssp(matrix_info, start).to_lists()[1]

        self.assertListEqual(expect, result)

    def test_sssp_with_2_paths_to_1_node(self):
        matrix_info = [[0, 0, 1, 1, 4, 5],
                       [1, 4, 3, 5, 2, 2],
                       [3, 7, 2, 4, 2, 1]]
        start = 0

        expect = [0, 3, 8, 5, 7, 7]
        result = sssp(matrix_info, start).to_lists()[1]

        self.assertListEqual(expect, result)