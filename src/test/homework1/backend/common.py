import random
import unittest
import numpy as np
from src.main.homework1.backend.cpu_computing import compute_on_cpu
from src.main.homework1.backend.gpu_computing import compute_on_gpu
from src.test.homework1.backend.utils import get_pixmap


def get_random_filters():
    def get_dim():
        r = random.randint(1, 10)
        return r + 1 - r % 2

    result = []
    for _ in range(random.randint(1, 10)):
        h = get_dim()
        w = get_dim()
        result.append(list(map(lambda i: list(map(lambda j: random.randint(0, 10), range(w))), range(h))))

    return result


class Common(unittest.TestCase):
    def test_compute_with_pixmap_matrices_3x2_and_3x3_and_id_filter(self):
        pixmaps_matrices = [get_pixmap(3, 2), get_pixmap(3, 3)]
        filters_matrices = [[[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]]

        cpu_result = compute_on_cpu(pixmaps_matrices, filters_matrices)
        gpu_result = compute_on_gpu(pixmaps_matrices, filters_matrices)

        map(lambda i: self.assertTrue(np.array_equal(cpu_result[i], gpu_result[i])), range(len(cpu_result)))

    def test_compute_on_gpu_with_pixmap_matrices_3x2_and_1x3_and_filters_3x3_and_1x5(self):
        pixmaps_matrices = [get_pixmap(3, 2), get_pixmap(1, 3)]
        filters_matrices = [[[0, 0, 0], [0, 2, 0], [0, 0, 0]], [[1, 1, 1, 1, 1]]]

        cpu_result = compute_on_cpu(pixmaps_matrices, filters_matrices)
        gpu_result = compute_on_gpu(pixmaps_matrices, filters_matrices)

        map(lambda i: self.assertTrue(np.array_equal(cpu_result[i], gpu_result[i])), range(len(cpu_result)))

    def test_compute_on_gpu_with_random_pixmaps_and_random_filters(self):
        pixmaps_matrices = list(map(lambda i: get_pixmap(random.randint(1, 10), random.randint(1, 10)),
                                    range(random.randint(0, 10))))
        filters_matrices = get_random_filters()

        cpu_result = compute_on_cpu(pixmaps_matrices, filters_matrices)
        gpu_result = compute_on_gpu(pixmaps_matrices, filters_matrices)

        map(lambda i: self.assertTrue(np.array_equal(cpu_result[i], gpu_result[i])), range(len(cpu_result)))



