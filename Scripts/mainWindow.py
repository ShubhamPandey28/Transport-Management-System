from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import RepairTab


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.setObjectName("MainWindow")
        self.resize(600, 400)

        self.setupUi()

    def setupUi(self):
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # Grid Layout will Not allow the window to be shorter than its widgets
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QRect(20, 10, 561, 361))
        self.tabWidget.setObjectName("tabWidget")

        self.repairTab = QWidget()
        self.repairTab.setObjectName("repairTab")

        HBox = QHBoxLayout(self.repairTab)
        self.repairForm = RepairTab.RepairForm(self)

        HBox.addWidget(self.repairForm)
        self.tabWidget.addTab(self.repairTab, "")

        # self.tab_2 = QWidget()
        # self.tab_2.setObjectName("tab_2")
        # self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)

        # self.statusbar = QStatusBar(self)
        # self.statusbar.setObjectName("statusbar")
        # selfsetStatusBar(self.statusbar)

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.repairForm.retranslateUi()
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.repairTab),
            _translate("MainWindow", "New Entry"),
        )
        # self.tabWidget.setTabText(
        #     self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "View History")
        # )


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
