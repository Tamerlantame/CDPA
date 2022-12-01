import unittest
import numpy as np
from src.main.homework1.backend.gpu_computing import apply_filters_to_matrix, compute_on_gpu
from src.test.homework1.backend.utils import get_pixmap, e


class GpuComputing(unittest.TestCase):
    def test_apply_filters_to_matrix_with_id_filters(self):
        pixmap = get_pixmap(115, 135)
        filters = list(map(lambda i: [[0, 0, 0], [0, 1, 0], [0, 0, 0]], range(5)))

        expect = pixmap
        result = apply_filters_to_matrix(pixmap, filters)

        self.assertTrue(np.array_equal(expect, result))

    def test_apply_filters_to_matrix_with_pixel_matrix_3x4_and_2_filters(self):
        pixmap = get_pixmap(3, 4)
        filters = [[[0, 0, 0], [0, 2, 0], [0, 0, 0]], [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]]

        expect = np.array([[e(54, 0), e(90, 1), e(108, 2), e(78, 3)],
                           [e(54, 4), e(90, 5), e(108, 6), e(78, 7)],
                           [e(54, 8), e(90, 9), e(108, 10), e(78, 11)]])

        result = apply_filters_to_matrix(pixmap, filters)

        self.assertTrue(np.array_equal(expect, result))

    def test_compute_on_gpu_with_pixmap_matrices_3x2_and_3x3_and_id_filter(self):
        pixmaps_matrices = [get_pixmap(3, 2), get_pixmap(3, 3)]
        filters_matrices = [[[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]]

        expect = [pixmaps_matrices[0], pixmaps_matrices[1]]
        result = compute_on_gpu(pixmaps_matrices, filters_matrices)

        map(lambda i: self.assertTrue(np.array_equal(expect[i], result[i])), range(len(expect)))

    def test_compute_on_gpu_with_pixmap_matrices_3x2_and_1x3_and_filters_3x3_and_1x5(self):
        pixmaps_matrices = [get_pixmap(3, 2), get_pixmap(1, 3)]
        filters_matrices = [[[0, 0, 0], [0, 2, 0], [0, 0, 0]], [[1, 1, 1, 1, 1]]]

        expect = [np.array([[e(4, 0), e(6, 1)],
                            [e(24, 2), e(26, 3)],
                            [e(44, 4), e(46, 5)]]),
                  np.array([[e(6, 0), e(10, 1), e(14, 2)]])]

        result = compute_on_gpu(pixmaps_matrices, filters_matrices)

        map(lambda i: self.assertTrue(np.array_equal(expect[i], result[i])), range(len(expect)))
