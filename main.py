__author__ = "Ashwin Ginoria"
__email__ = "ashwinginoria@gmail.com"

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt
# import sqlite3


# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    # constructor for python
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("SG Transport")

        label = QLabel("Created by Ashwin Ginoria and Shubham Pandey!! :)")

        # The `Qt` namespace has a lot of attributes to customise
        # widgets. See: http://doc.qt.io/qt-5/qt.html
        label.setAlignment(Qt.AlignCenter)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(label)


def main():
    app = QApplication(sys.argv)

    # Creating a Window
    window = MainWindow()
    window.show()

    # Executing the app
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
