import numpy as np


def e(main_value, addition_value=None):
    result = list(map(lambda i: main_value, range(3)))

    if addition_value is None:
        result.append(main_value)
    else:
        result.append(addition_value)

    return result


def get_pixmap(h, w):
    return np.array(list(map(lambda i: list(map(lambda j: e(w * i + j), range(w))), range(h))), dtype=np.uint8)
