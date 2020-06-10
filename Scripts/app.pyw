from PyQt5.QtWidgets import *
import mainWindow

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = mainWindow.MainWindow()
    ui.show()
    sys.exit(app.exec_())
