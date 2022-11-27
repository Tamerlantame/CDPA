from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget

from src.main.homework1 import config
from src.main.homework1.frontend.utils import center


class SavedView(QMainWindow):
    def __init__(self, previous_view):
        def configure_main_widget():
            def configure_main_layout():
                def ok_button_click():
                    previous_view.show()
                    self.hide()

                description = QLabel()
                description.setText(f"Successfully saved to {config.directory_to_save}")

                ok_button = QPushButton("OK")
                ok_button.clicked.connect(ok_button_click)

                main_layout = QVBoxLayout()
                main_layout.addWidget(description)
                main_layout.addWidget(ok_button)

                return main_layout

            main_widget = QWidget()
            main_widget.setLayout(configure_main_layout())

            return main_widget

        super().__init__()
        self.setWindowTitle("Filters")
        center(self)
        self.setCentralWidget(configure_main_widget())
