from PyQt5.QtWidgets import QDesktopWidget


def center(item):
    qr = item.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    item.move(qr.topLeft())
