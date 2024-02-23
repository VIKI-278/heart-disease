import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox
from mainwin import MainUI

app = QtWidgets.QApplication(sys.argv)
window = MainUI()
window.showMaximized()
sys.exit(app.exec())



