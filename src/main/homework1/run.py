import sys
from PyQt5.QtWidgets import QApplication
from main_view import MainView

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainView().show()
    sys.exit(app.exec_())
