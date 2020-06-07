from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import RepairTab


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.setObjectName("MainWindow")
        self.setWindowTitle("MainWindow")
        self.resize(600, 400)

        self.setupUi()

    def setupUi(self):
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # Grid Layout will Not allow the window to be shorter than its widgets
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # Setting up Tab Widget
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QRect(20, 10, 550, 350))
        self.tabWidget.setObjectName("tabWidget")

        # Tab 1
        self.repairTab = QWidget()
        self.repairTab.setObjectName("repairTab")
        self.tabWidget.addTab(self.repairTab, "")
        self.tabWidget.setTabText(0, "New Entry")
        self.repairForm = RepairTab.RepairForm(self)

        HBox = QHBoxLayout(self.repairTab)
        HBox.addWidget(self.repairForm)

        # Tab 2
        # self.tab_2 = QWidget()
        # self.tab_2.setObjectName("tab_2")
        # self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)

        self.tabWidget.setCurrentIndex(0)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
