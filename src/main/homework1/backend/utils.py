import numpy as np
from PyQt5.QtGui import QPixmap, QImage


def pixmap_to_image_with_format(pixmap):
    width = pixmap.width()
    height = pixmap.height()

    image = pixmap.toImage()
    channels = 4
    bit_string = image.bits().asstring(width * height * channels)

    return np.frombuffer(bit_string, dtype=np.uint8).reshape((height, width, channels)), image.format()


def matrix_to_pixmap(matrix, image_format):
    height, width, _ = matrix.shape

    return QPixmap(QImage(matrix.data, width, height, 4 * width, image_format))
