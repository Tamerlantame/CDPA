from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QWidget
from src.main.homework1 import config
from src.main.homework1.backend import computing, folder_computing
from src.main.homework1.frontend.create_filter_view import CreateFilterView
from src.main.homework1.frontend.saved_view import SavedView
from src.main.homework1.frontend.two_pictures_view import TwoPicturesView
from src.main.homework1.frontend.utils import center


class FiltersView(QMainWindow):
    def __init__(self, previous_view, p, is_file_mode):
        def configure_main_widget():
            def configure_main_layout():
                def configure_filters_layout():
                    description = QLabel()
                    description.setText("Chosen filters:")

                    filters_layout = QVBoxLayout()
                    filters_layout.addWidget(description)
                    filters_layout.addLayout(filters_list_layout)

                    return filters_layout

                def configure_menu_layout():
                    def configure_change_filters_layout():
                        def add_filter(matrix, text):
                            filters_matrices_list.append(matrix)

                            label = QLabel()
                            label.setText(text)
                            filters_list_layout.addWidget(label)

                        def filter1_button_click():
                            add_filter(config.filter1_matrix, "Filter 1")

                        def filter2_button_click():
                            add_filter(config.filter2_matrix, "Filter 2")

                        def create_filter_button_click():
                            CreateFilterView(self, filters_matrices_list, filters_list_layout).show()
                            self.hide()

                        def cancel_button_click():
                            if len(filters_matrices_list) != 0:
                                filters_matrices_list.pop()
                                filters_list_layout.itemAt(filters_list_layout.count() - 1).widget().deleteLater()

                        filter1_button = QPushButton("Filter 1")
                        filter1_button.clicked.connect(filter1_button_click)

                        filter2_button = QPushButton("Filter 2")
                        filter2_button.clicked.connect(filter2_button_click)

                        create_filter_button = QPushButton("Create filter")
                        create_filter_button.clicked.connect(create_filter_button_click)

                        cancel_button = QPushButton("Cancel last")
                        cancel_button.clicked.connect(cancel_button_click)

                        change_filters_layout = QVBoxLayout()
                        change_filters_layout.addWidget(filter1_button)
                        change_filters_layout.addWidget(filter2_button)
                        change_filters_layout.addWidget(create_filter_button)
                        change_filters_layout.addWidget(cancel_button)

                        return change_filters_layout

                    def configure_main_buttons_layout():
                        def configure_computing_buttons_layout():
                            def display_result(on_cpu):
                                if is_file_mode:
                                    result = computing.compute(p, filters_matrices_list, on_cpu)
                                    TwoPicturesView(previous_view, result[0][0], result[0][1]).show()
                                else:
                                    folder_computing.compute(p, filters_matrices_list, on_cpu)
                                    SavedView(previous_view).show()

                                self.hide()

                            def cpu_button_click():
                                display_result(True)

                            def gpu_button_click():
                                display_result(False)

                            cpu_button = QPushButton("Compute using CPU")
                            cpu_button.clicked.connect(cpu_button_click)

                            gpu_button = QPushButton("Compute using GPU")
                            gpu_button.clicked.connect(gpu_button_click)

                            computing_buttons_layout = QHBoxLayout()
                            computing_buttons_layout.addWidget(cpu_button)
                            computing_buttons_layout.addWidget(gpu_button)

                            return computing_buttons_layout

                        def back_button_click():
                            previous_view.show()
                            self.hide()

                        back_button = QPushButton("Back")
                        back_button.clicked.connect(back_button_click)

                        main_buttons_layout = QVBoxLayout()
                        main_buttons_layout.addLayout(configure_computing_buttons_layout())
                        main_buttons_layout.addWidget(back_button)

                        return main_buttons_layout

                    filters_matrices_list = []

                    menu_layout = QVBoxLayout()
                    menu_layout.addLayout(configure_change_filters_layout())
                    menu_layout.addLayout(configure_main_buttons_layout())

                    return menu_layout

                filters_list_layout = QVBoxLayout()

                main_layout = QHBoxLayout()
                main_layout.addLayout(configure_filters_layout())
                main_layout.addLayout(configure_menu_layout())

                return main_layout

            main_widget = QWidget()
            main_widget.setLayout(configure_main_layout())

            return main_widget

        super().__init__()
        self.setWindowTitle("Filters")
        center(self)
        self.setCentralWidget(configure_main_widget())
