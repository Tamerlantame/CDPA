import unittest
import numpy as np
from src.main.homework1.backend.cpu_computing import get_intermediate_matrix, apply_filter_to_one_element, \
    apply_filters_to_matrix, compute_on_cpu
from src.test.homework1.backend.utils import get_pixmap, e



class CpuComputing(unittest.TestCase):
    def test_get_intermediate_matrix_with_pixmap_3x3_and_filter_3x5(self):
        pixmap = get_pixmap(3, 3)
        pixmap_height, pixmap_width, _ = pixmap.shape

        filter_height, filter_width = 3, 5

        expect = np.array([[e(0), e(0), e(0), e(1), e(2), e(2), e(2)],
                           [e(0), e(0), e(0), e(1), e(2), e(2), e(2)],
                           [e(3), e(3), e(3), e(4), e(5), e(5), e(5)],
                           [e(6), e(6), e(6), e(7), e(8), e(8), e(8)],
                           [e(6), e(6), e(6), e(7), e(8), e(8), e(8)]])
        result = get_intermediate_matrix(pixmap, pixmap_height, pixmap_width, filter_height, filter_width)

        self.assertTrue(np.array_equal(expect, result))

    def test_get_intermediate_matrix_with_pixmap_2x3_and_filter_3x3(self):
        pixmap = get_pixmap(2, 3)
        pixmap_height, pixmap_width, _ = pixmap.shape

        filter_height, filter_width = 3, 3

        expect = np.array([[e(0), e(0), e(1), e(2), e(2)],
                           [e(0), e(0), e(1), e(2), e(2)],
                           [e(3), e(3), e(4), e(5), e(5)],
                           [e(3), e(3), e(4), e(5), e(5)]])
        result = get_intermediate_matrix(pixmap, pixmap_height, pixmap_width, filter_height, filter_width)

        self.assertTrue(np.array_equal(expect, result))

    def test_get_intermediate_matrix_with_pixmap_4x2_and_filter_3x1(self):
        pixmap = get_pixmap(4, 2)
        pixmap_height, pixmap_width, _ = pixmap.shape

        filter_height, filter_width = 3, 1

        expect = np.array([[e(0), e(1)],
                           [e(0), e(1)],
                           [e(2), e(3)],
                           [e(4), e(5)],
                           [e(6), e(7)],
                           [e(6), e(7)]])
        result = get_intermediate_matrix(pixmap, pixmap_height, pixmap_width, filter_height, filter_width)

        self.assertTrue(np.array_equal(expect, result))

    def test_apply_filter_to_one_element_with_first_line_first_row(self):
        intermediate_matrix = np.array([[e(0), e(0), e(0), e(1), e(2), e(2), e(2)],
                                        [e(0), e(0), e(0), e(1), e(2), e(2), e(2)],
                                        [e(3), e(3), e(3), e(4), e(5), e(5), e(5)],
                                        [e(6), e(6), e(6), e(7), e(8), e(8), e(8)],
                                        [e(6), e(6), e(6), e(7), e(8), e(8), e(8)]])
        current_filter = np.array([[1, 1, 1, 1, 1],
                                   [1, 1, 1, 1, 1],
                                   [1, 1, 1, 1, 1]])
        line_number = 0
        row_number = 0

        expect = [24, 24, 24, 0]
        result = apply_filter_to_one_element(intermediate_matrix, current_filter, line_number, row_number)

        self.assertListEqual(expect, result)

    def test_apply_filter_to_one_element_with_middle_line_middle_row(self):
        intermediate_matrix = np.array([[e(0), e(0), e(1), e(2), e(2)],
                                        [e(0), e(0), e(1), e(2), e(2)],
                                        [e(3), e(3), e(4), e(5), e(5)],
                                        [e(6), e(6), e(7), e(8), e(8)],
                                        [e(6), e(6), e(7), e(8), e(8)]])
        current_filter = np.array([[1, 1, 1],
                                   [1, 1, 1],
                                   [1, 1, 1]])
        line_number = 1
        row_number = 1

        expect = [36, 36, 36, 4]
        result = apply_filter_to_one_element(intermediate_matrix, current_filter, line_number, row_number)

        self.assertListEqual(expect, result)

    def test_apply_filter_to_one_element_with_last_line_last_row(self):
        intermediate_matrix = np.array([[e(0), e(0), e(0), e(1), e(2), e(2), e(2)],
                                        [e(0), e(0), e(0), e(1), e(2), e(2), e(2)],
                                        [e(3), e(3), e(3), e(4), e(5), e(5), e(5)],
                                        [e(6), e(6), e(6), e(7), e(8), e(8), e(8)],
                                        [e(6), e(6), e(6), e(7), e(8), e(8), e(8)]])
        current_filter = np.array([[1, 1, 1, 1, 1],
                                   [1, 1, 1, 1, 1],
                                   [1, 1, 1, 1, 1]])
        line_number = 2
        row_number = 2

        expect = [96, 96, 96, 8]
        result = apply_filter_to_one_element(intermediate_matrix, current_filter, line_number, row_number)

        self.assertListEqual(expect, result)

    def test_apply_filters_to_matrix_with_id_filters(self):
        pixmap = get_pixmap(15, 135)
        filters = list(map(lambda i: [[0, 0, 0], [0, 1, 0], [0, 0, 0]], range(5)))

        expect = pixmap
        result = apply_filters_to_matrix(pixmap, filters)

        self.assertTrue(np.array_equal(expect, result))

    def test_apply_filters_to_matrix_with_pixel_matrix_3x3_and_2_filters(self):
        pixmap = get_pixmap(3, 3)
        filters = [[[0, 0, 0], [0, 2, 0], [0, 0, 0]], [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]]

        expect = np.array([[e(48, 0), e(60, 1), e(72, 2)],
                           [e(108, 3), e(120, 4), e(132, 5)],
                           [e(168, 6), e(180, 7), e(192, 8)]])

        result = apply_filters_to_matrix(pixmap, filters)

        self.assertTrue(np.array_equal(expect, result))

    def test_compute_on_cpu_with_pixmap_matrices_3x2_and_3x3_and_id_filter(self):
        pixmaps_matrices = [get_pixmap(3, 2), get_pixmap(3, 3)]
        filters_matrices = [[[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]]

        expect = [pixmaps_matrices[0], pixmaps_matrices[1]]
        result = compute_on_cpu(pixmaps_matrices, filters_matrices)

        map(lambda i: self.assertTrue(np.array_equal(expect[i], result[i])), range(len(expect)))

    def test_compute_on_cpu_with_pixmap_matrices_3x2_and_1x3_and_filters_3x3_and_1x5(self):
        pixmaps_matrices = [get_pixmap(3, 2), get_pixmap(1, 3)]
        filters_matrices = [[[0, 0, 0], [0, 2, 0], [0, 0, 0]], [[1, 1, 1, 1, 1]]]

        expect = [np.array([[e(4, 0), e(6, 1)],
                            [e(24, 2), e(26, 3)],
                            [e(44, 4), e(46, 5)]]),
                  np.array([[e(6, 0), e(10, 1), e(14, 2)]])]

        result = compute_on_cpu(pixmaps_matrices, filters_matrices)

        map(lambda i: self.assertTrue(np.array_equal(expect[i], result[i])), range(len(expect)))
