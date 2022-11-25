import os
from os import listdir
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QWidget
import config
from saved_view import SavedView
from utils import center


class TwoPicturesView(QMainWindow):
    def __init__(self, previous_view, pixmap_without_filters, pixmap_with_filters):
        def configure_main_widget():
            def configure_main_layout():
                def configure_pictures_layout():
                    def configure_picture_layout(description, pixmap):
                        description_label = QLabel()
                        description_label.setText(description)

                        picture_label = QLabel()
                        picture_label.setPixmap(pixmap)

                        picture_layout = QVBoxLayout()
                        picture_layout.addWidget(description_label)
                        picture_layout.addWidget(picture_label)

                        return picture_layout

                    pictures_layout = QHBoxLayout()
                    pictures_layout \
                        .addLayout(configure_picture_layout("Picture without filters", pixmap_without_filters))
                    pictures_layout \
                        .addLayout(configure_picture_layout("Picture with filters", pixmap_with_filters))

                    return pictures_layout

                def configure_menu_layout():
                    def save_button_click():
                        path = config.directory_to_save
                        if not os.path.exists(path):
                            os.mkdir(path)

                        pixmap_with_filters.save(f"{path}/file{len(listdir(path))}.png")

                        SavedView(self).show()
                        self.hide()

                    def back_button_click():
                        previous_view.show()
                        self.hide()

                    save_button = QPushButton("Save result")
                    save_button.clicked.connect(save_button_click)

                    back_button = QPushButton("Back")
                    back_button.clicked.connect(back_button_click)

                    menu_layout = QHBoxLayout()
                    menu_layout.addWidget(save_button)
                    menu_layout.addWidget(back_button)

                    return menu_layout

                main_layout = QVBoxLayout()
                main_layout.addLayout(configure_pictures_layout())
                main_layout.addLayout(configure_menu_layout())

                return main_layout

            main_widget = QWidget()
            main_widget.setLayout(configure_main_layout())

            return main_widget

        super().__init__()
        self.setWindowTitle("Filters")
        center(self)
        self.setCentralWidget(configure_main_widget())
