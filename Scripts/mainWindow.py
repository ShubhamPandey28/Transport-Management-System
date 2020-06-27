from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from .RepairTab import RepairForm
from .AddConsignmentTab import AddConsignmentForm
from .AddConsignor import AddConsignorDlg
from .BillGenerateTab import BillForm
from .ViewTable import debugView


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.setObjectName("MainWindow")
        self.setWindowTitle("SG Transport")
        self.resize(600, 400)

        self.setupUi()

    def setupUi(self):

        # Set-Up Menu Bar
        self.menubar = QMenuBar(self)
        self.menuMenu = QMenu(self.menubar, title="Menu")
        self.debugMenu = QMenu(self.menubar, title="Debug")
        self.setMenuBar(self.menubar)

        # Add Consignee Menu option
        self.actionAddConsignee = QAction("Add Consignee", self)
        self.menuMenu.addAction(self.actionAddConsignee)
        self.actionAddConsignee.triggered.connect(lambda: self.openAddConsignorWindow())

        # Creating Debug Menu Options
        self.actionViewConsignments = QAction("View Consignments", self)
        self.debugMenu.addAction(self.actionViewConsignments)
        self.actionViewConsignments.triggered.connect(lambda: self.viewTable("Consignment"))

        self.actionViewClients = QAction("View Cliets", self)
        self.debugMenu.addAction(self.actionViewClients)
        self.actionViewClients.triggered.connect(lambda: self.viewTable("Consignor_Consignee"))

        self.actionViewVehicles = QAction("View Vehicles", self)
        self.debugMenu.addAction(self.actionViewVehicles)
        self.actionViewVehicles.triggered.connect(lambda: self.viewTable("Vehicle"))

        self.actionViewRepair = QAction("View Repair Log", self)
        self.debugMenu.addAction(self.actionViewRepair)
        self.actionViewRepair.triggered.connect(lambda: self.viewTable("Repair_Log"))

        self.actionViewBills = QAction("View Bills", self)
        self.debugMenu.addAction(self.actionViewBills)
        self.actionViewBills.triggered.connect(lambda: self.viewTable("Bills"))
        

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.debugMenu.menuAction())

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
        self.repairForm = RepairForm(self)
        HBox = QHBoxLayout(self.repairTab)
        HBox.addWidget(self.repairForm)

        # Tab 2
        self.addConsinmentTab = QWidget(self.tabWidget)
        self.addConsinmentTab.setObjectName("addConsinmentTab")
        self.tabWidget.addTab(self.addConsinmentTab, "Add Consignment")
        self.consignmentForm = AddConsignmentForm(self)
        HBox = QHBoxLayout(self.addConsinmentTab)
        HBox.addWidget(self.consignmentForm)

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)

        # Tab 3
        self.billGenTab = QWidget(self.tabWidget)
        self.billGenTab.setObjectName("billGenTab")
        self.tabWidget.addTab(self.billGenTab, "Generate Bill")
        self.billForm = BillForm(self)
        HBox = QHBoxLayout(self.billGenTab)
        HBox.addWidget(self.billForm)

        # Set-up StatusBar
        # self.statusbar = QtWidgets.QStatusBar(self)
        # self.statusbar.setObjectName("statusbar")
        # self.setStatusBar(self.statusbar)
        self.statusBar().showMessage("Status: Ready")

        self.tabWidget.setCurrentIndex(0)

    def openAddConsignorWindow(self):
        self.ui = AddConsignorDlg()
        self.ui.show()

    def viewTable(self, table_name):
        self.ui = debugView(table_name)
        self.ui.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
