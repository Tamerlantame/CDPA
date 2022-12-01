import cupy as cp
from cupyx.scipy.signal import convolve2d


def apply_filters_to_matrix(pixmap_matrix, filters_matrices):
    def apply_filter_to_one_channel(filter_matrix, channel):
        if channel == 3:
            result = current_pixmap[0: height, 0: width, 3]
        else:
            result = convolve2d(current_pixmap[0: height, 0: width, channel], cp.array(filter_matrix), mode="same")

        return result

    height, width, _ = pixmap_matrix.shape

    current_pixmap = cp.asarray(pixmap_matrix)
    for f in filters_matrices:
        current_pixmap = cp.transpose(
            cp.array(list(map(lambda ch: apply_filter_to_one_channel(f, ch), range(4))), dtype=cp.uint8), (1, 2, 0))

    return cp.asnumpy(current_pixmap)


def compute_on_gpu(pixmap_matrices, filters_matrices):
    return list(map(lambda p: apply_filters_to_matrix(p, filters_matrices), pixmap_matrices))
