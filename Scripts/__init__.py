import sys

from PyQt5.QtWidgets import QApplication
from .mainWindow import MainWindow

app = QApplication(sys.argv)
ui = MainWindow()

__all__ = [app, ui]
