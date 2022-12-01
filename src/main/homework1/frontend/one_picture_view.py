from PyQt5 import QtGui
from PyQt5.QtCore import QFileInfo
from PyQt5.QtWidgets import QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout

from src.main.homework1.frontend.filters_view import FiltersView
from src.main.homework1.frontend.utils import center


class OnePictureView(QMainWindow):
    def __init__(self, previous_view, picture):
        def configure_main_widget():
            def configure_main_layout():
                def configure_picture_layout():
                    description = QLabel()
                    description.setText("Chosen picture:")

                    picture_label = QLabel()
                    picture_label.setPixmap(pixmap)

                    picture_layout = QVBoxLayout()
                    picture_layout.addWidget(description)
                    picture_layout.addWidget(picture_label)

                    return picture_layout

                def configure_menu_layout():
                    def configure_info_layout():
                        pixels_size = pixmap.width() * pixmap.height()

                        pixels_size_label = QLabel()
                        pixels_size_label.setText(f"Size in pixels: {pixels_size}")

                        bytes_size_label = QLabel()
                        bytes_size_label.setText(f"Size in bytes: {QFileInfo(picture).size()}")

                        info_layout = QVBoxLayout()
                        info_layout.addWidget(pixels_size_label)
                        info_layout.addWidget(bytes_size_label)

                        return info_layout

                    def configure_buttons_layout():
                        def back_button_click():
                            previous_view.show()
                            self.hide()

                        def apply_button_click():
                            FiltersView(self, [pixmap], True).show()
                            self.hide()

                        apply_button = QPushButton("Apply some filters")
                        apply_button.clicked.connect(apply_button_click)

                        back_button = QPushButton("Back")
                        back_button.clicked.connect(back_button_click)

                        buttons_layout = QHBoxLayout()
                        buttons_layout.addWidget(apply_button)
                        buttons_layout.addWidget(back_button)

                        return buttons_layout

                    menu_layout = QVBoxLayout()
                    menu_layout.addLayout(configure_info_layout())
                    menu_layout.addLayout(configure_buttons_layout())

                    return menu_layout

                pixmap = QtGui.QPixmap(picture)

                main_layout = QHBoxLayout()
                main_layout.addLayout(configure_picture_layout())
                main_layout.addLayout(configure_menu_layout())

                return main_layout

            main_widget = QWidget()
            main_widget.setLayout(configure_main_layout())

            return main_widget

        super().__init__()
        self.setWindowTitle("Filters")
        center(self)
        self.setCentralWidget(configure_main_widget())
