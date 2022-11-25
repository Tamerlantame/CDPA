import numpy as np


def get_intermediate_matrix(pixmap, pixmap_height, pixmap_width, filter_height, filter_width):
    def get_intermediate_matrix_line(line_number):
        def get_index_in_pixmap_matrix(matrix_dim, filter_dim, cur_index):
            addition_dim = filter_dim // 2

            if cur_index <= addition_dim:
                index = 0
            elif addition_dim < cur_index < addition_dim + matrix_dim:
                index = cur_index - addition_dim
            else:
                index = matrix_dim - 1

            return index

        line_index = get_index_in_pixmap_matrix(pixmap_height, filter_height, line_number)

        return list(map(lambda i: pixmap[line_index][get_index_in_pixmap_matrix(pixmap_width, filter_width, i)],
                        range(pixmap_width + filter_width - 1)))

    return np.array(list(map(get_intermediate_matrix_line, range(pixmap_height + filter_height - 1))), dtype=np.uint8)


def apply_filter_to_one_element(intermediate_matrix, current_filter, line_number, row_number):
    def get_cur_element(d):
        if d == 3:
            cur = intermediate_matrix[line_number + h // 2, row_number + w // 2, 3]
        else:
            cur = np.sum(np.multiply(intermediate_matrix[line_number: line_number + h, row_number: row_number + w, d],
                                     current_filter))

            if cur < 0 or cur > 255:
                cur = cur % 255

        return cur

    h, w = current_filter.shape

    return list(map(get_cur_element, range(4)))


def apply_filters_to_matrix(pixmap_matrix, filters_matrices):
    def apply_filter_to_line(intermediate_matrix, filter_matrix, line_number, rows_numbers):
        return list(map(lambda n: apply_filter_to_one_element(intermediate_matrix, filter_matrix, line_number, n),
                        rows_numbers))

    pixmap_height, pixmap_width, _ = pixmap_matrix.shape

    current_pixmap = pixmap_matrix
    for f in filters_matrices:
        intermediate = get_intermediate_matrix(current_pixmap, pixmap_height, pixmap_width, len(f), len(f[0]))

        current_pixmap = np.array(
            list(map(lambda n: apply_filter_to_line(intermediate, np.array(f), n, range(pixmap_width)),
                     range(pixmap_height))),
            dtype=np.uint8)

    return current_pixmap


def compute_on_cpu(pixmap_matrices, filters_matrices):
    return list(map(lambda p: apply_filters_to_matrix(p, filters_matrices), pixmap_matrices))
