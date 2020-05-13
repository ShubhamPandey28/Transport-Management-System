__author__ = "Ashwin Ginoria"
__email__ = "ashwinginoria@gmail.com"

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow


# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):
    # Properties of the window like title goes here
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("SG Transport")
        self.initUI()

    # All UI elements in Main-Window to be modified here
    def initUI(self):
        self.label = QLabel(self)
        self.label.setText("Created by Ashwin Ginoria and Shubham Pandey!! :)")
        # self.label.move(50, 50)

        # The `Qt` namespace has a lot of attributes to customise
        # widgets. See: http://doc.qt.io/qt-5/qt.html
        self.label.setAlignment(Qt.AlignCenter)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(self.label)


def main():
    # sys.argv provides with information about the OS for themeing
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
