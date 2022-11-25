from PyQt5.QtWidgets import QWidget, QPushButton, QMainWindow, QVBoxLayout, QFileDialog
from filters_view import FiltersView
from one_picture_view import OnePictureView
from utils import center


class MainView(QMainWindow):
    def __init__(self):
        def configure_main_widget():
            def configure_main_layout():
                def picture_button_click():
                    picture = \
                        QFileDialog.getOpenFileName(caption="Choose a file", filter="Images (*.png *.jpg *.jpeg)")[0]
                    if picture != "":
                        OnePictureView(self, picture).show()
                        self.hide()

                def directory_button_click():
                    path = QFileDialog.getExistingDirectory(caption="Choose a directory")
                    if path != "":
                        FiltersView(self, path, False).show()
                        self.hide()

                picture_button = QPushButton("Work with one picture")
                picture_button.clicked.connect(picture_button_click)

                directory_button = QPushButton("Work with directory")
                directory_button.clicked.connect(directory_button_click)

                main_layout = QVBoxLayout()
                main_layout.addWidget(picture_button)
                main_layout.addWidget(directory_button)

                return main_layout

            main_widget = QWidget()
            main_widget.setLayout(configure_main_layout())

            return main_widget

        super().__init__()
        self.setWindowTitle("Filters")
        center(self)
        self.setCentralWidget(configure_main_widget())
