from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import RepairTab
import AddConsignmentTab
from AddConsignor import Ui_AddConsignorDlg
from AddVehicle import AddVehicleform


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.setObjectName("MainWindow")
        self.setWindowTitle("MainWindow")
        self.resize(600, 400)

        self.setupUi()

    def setupUi(self):

        # Set-Up Menu Bar
        self.menubar = QMenuBar(self)
        self.menubar.setObjectName("menubar")
        self.menuMenu = QMenu(self.menubar, title="Menu")
        self.menuMenu.setObjectName("menuMenu")
        self.setMenuBar(self.menubar)

        # Add Consignee Menu option
        self.actionAddConsignee = QAction("Add Consignee", self)
        self.actionAddConsignee.setObjectName("actionAddConsignee")
        # self.actionAddConsignee.statusTip("Add a new Consigner/Consignee")
        # self.actionAddConsignee.triggered.connect(AddConsignor.show_dlg())
        self.menuMenu.addAction(self.actionAddConsignee)

        self.actionAddVehicle = QAction("Add Vehicle",self)
        self.actionAddConsignee.setObjectName("actionAddVehicle")
        self.menuMenu.addAction(self.actionAddVehicle)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.actionAddConsignee.triggered.connect(lambda : self.openAddConsignorWindow())
        self.actionAddVehicle.triggered.connect(lambda : self.openAddVehicleWindow())


        # Set-Up Central Widget
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
        self.repairTab = QWidget(self.tabWidget)
        self.repairTab.setObjectName("repairTab")
        self.tabWidget.addTab(self.repairTab, "New Entry")
        self.repairForm = RepairTab.RepairForm(self)
        HBox = QHBoxLayout(self.repairTab)
        HBox.addWidget(self.repairForm)

        # Tab 2
        self.addConsinmentTab = QWidget(self.tabWidget)
        self.addConsinmentTab.setObjectName("addConsinmentTab")
        self.tabWidget.addTab(self.addConsinmentTab, "Add Consignment")
        self.consignmentForm = AddConsignmentTab.AddConsignmentForm(self)
        HBox = QHBoxLayout(self.addConsinmentTab)
        HBox.addWidget(self.consignmentForm)

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)

        # Set-up StatusBar
        # self.statusbar = QtWidgets.QStatusBar(self)
        # self.statusbar.setObjectName("statusbar")
        # self.setStatusBar(self.statusbar)
        self.statusBar().showMessage("Status: Ready")

        self.tabWidget.setCurrentIndex(0)
    
    def openAddConsignorWindow(self):
        self.ui = Ui_AddConsignorDlg()
        self.ui.show()

    def openAddVehicleWindow(self):
        self.ui = AddVehicleform()
        self.ui.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
