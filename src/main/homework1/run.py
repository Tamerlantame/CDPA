import sys
from PyQt5.QtWidgets import QApplication
from src.main.homework1.frontend.main_view import MainView

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainView().show()
    sys.exit(app.exec_())
