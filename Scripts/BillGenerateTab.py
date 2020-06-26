from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from .pdfGen import saveBill


class BillForm(QGroupBox):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.setObjectName("BillTab")
        self.setWindowTitle("Generate New Bill")

        self.setupUi()

    def setupUi(self):
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")

        self.nameLabel = QLabel("&Client", self)
        self.nameLabel.setObjectName("nameLabel")
        self.nameLineEdit = QLineEdit(self)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.nameLineEdit.textChanged.connect(self.updateConsignments)
        self.nameLabel.setBuddy(self.nameLineEdit)

        self.consignmentLabel = QLabel("Consignment &No.", self)
        self.consignmentLabel.setObjectName("consignmentLabel")
        self.consignmentLineEdit = QLineEdit(self)
        self.consignmentLineEdit.setObjectName("consignmentLineEdit")
        self.consignmentLabel.setBuddy(self.consignmentLineEdit)

        self.pushButton = QPushButton("Add Consignment", self)
        self.pushButton.setObjectName("pushButton")

        self.checkBoxSgst = QCheckBox("SGST", self)
        self.checkBoxSgst.setObjectName("checkBoxSgst")

        self.checkBoxCgst = QCheckBox("CGST", self)
        self.checkBoxCgst.setObjectName("checkBoxCgst")

        self.checkBoxIgst = QCheckBox("IGST", self)
        self.checkBoxIgst.setObjectName("checkBoxIgst")

        self.tableView = QTableView(self)
        self.tableView.setObjectName("ItemsView")

        self.tableButtons = QTableView(self)
        self.tableButtons.setObjectName("RemoveButtons")
        self.tableButtons.setFixedWidth(30)

        self.tableLayout = QHBoxLayout()
        self.tableLayout.setObjectName("tableLayout")
        self.tableLayout.addWidget(self.tableView)
        self.tableLayout.addWidget(self.tableButtons)

        self.buttonGenerateBill = QPushButton("Generate Bill", self)
        self.buttonGenerateBill.setObjectName("buttonGenerateBill")
        self.buttonGenerateBill.clicked.connect(self.GenerateBill)

        self.gridLayout.addWidget(self.buttonGenerateBill, 8, 1, 1, 3)
        self.gridLayout.addLayout(self.tableLayout, 7, 0, 1, 5)
        self.gridLayout.addWidget(self.checkBoxSgst, 4, 4, 1, 1)
        self.gridLayout.addWidget(self.checkBoxCgst, 5, 4, 1, 1)
        self.gridLayout.addWidget(self.checkBoxIgst, 6, 4, 1, 1)
        self.gridLayout.addWidget(self.nameLabel, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.nameLineEdit, 4, 1, 1, 2)
        self.gridLayout.addWidget(self.consignmentLabel, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.consignmentLineEdit, 5, 1, 1, 2)
        self.gridLayout.addWidget(self.pushButton, 6, 1, 1, 2)

        QMetaObject.connectSlotsByName(self)
        self.populateAutoComplete()

    @pyqtSlot()
    def updateConsignments(self):
        print("In Update")
        # response = getConsignmentByClient(self.nameLineEdit.text())

        # completer = QCompleter(response)
        # completer.setCaseSensitivity(Qt.CaseInsensitive)
        # self.consignmentLineEdit.setCompleter(completer)
        print("Done Update")

    def populateAutoComplete(self):
        print("In Populate")
        # response = show('Consignor_Consignee', {'Name': True})['result']

        # listOfClients = []
        # for row in response:
        #     listOfClients.append(row[0])

        # print(listOfClients)

        # completer = QCompleter(listOfClients)
        # completer.setCaseSensitivity(Qt.CaseInsensitive)
        # self.nameLineEdit.setCompleter(completer)
        print("Populate Done")

    @pyqtSlot()
    def GenerateBill(self):
        print("Generating Bill")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = BillForm()
    ui.show()
    sys.exit(app.exec_())
