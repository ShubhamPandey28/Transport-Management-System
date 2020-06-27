from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .itemsTableView import itemsTableView


class AddConsignmentForm(QGroupBox):
    def __init__(self, parent=None):
        super(AddConsignmentForm, self).__init__(parent)

        self.setObjectName("AddConsignmentTab")
        self.setMaximumSize(QSize(600, 600))
        # self.setMinimumSize()
        self.setWindowTitle("Generate Bill")

        self.setupUi()

    def setupUi(self):

        font = QFont()
        font.setPointSize(12)
        font = QFont()
        # font.setFamily("Ubuntu")
        font.setPointSize(12)
        # font.setBold(True)
        # font.setWeight(75)
        self.resize(1000, 800)
        self.setFont(font)

        self.qvLayout = QVBoxLayout()
        self.qvLayout.setObjectName("qvLayout")

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        # self.gridLayout.setColumnStretch(2,1)
        # self.gridLayout.setColumnStretch(3,1)

        self.addItemGrid = QGridLayout()
        self.addItemGrid.setObjectName("addItemGrid")
        headings = ["Description", "Packing", "Packages", "Weight"]
        self.itemsTable = itemsTableView(headings, 0, len(headings))

        self.fromLabel = QLabel("&From", self)
        self.fromLabel.setFont(font)
        self.fromLabel.setObjectName("fromLabel")
        self.fromCB = QComboBox(self)
        self.fromCB.setObjectName("fromCB")
        self.fromLabel.setBuddy(self.fromCB)
        self.fromCB.addItem("Kolkata-WB")
        self.fromCB.addItem("Meerut-UP")
        self.fromCB.addItem("Jaipur-Rajasthan")
        self.fromCB.addItem("Kota-Rajasthan")
        self.fromCB.addItem("Ahmedabad-Gujarat")

        self.destLabel = QLabel("&Destination", self)
        self.destLabel.setFont(font)
        self.destLabel.setObjectName("destLabel")
        self.destCB = QComboBox(self)
        self.destCB.setObjectName("destCB")
        self.destLabel.setBuddy(self.destCB)
        self.destCB.addItem("Kota-Rajansthan")
        self.destCB.addItem("Meerut-UP")
        self.destCB.addItem("Jaipur-Rajasthan")
        self.destCB.addItem("Ahmedabad-Gujarat")

        self.consignorLabel = QLabel("Consigno&r", self)
        self.consignorLabel.setFont(font)
        self.consignorLabel.setObjectName("consignorLabel")
        self.consignorCB = QComboBox(self)
        self.consignorCB.setObjectName("consignorCB")
        self.consignorLabel.setBuddy(self.consignorCB)
        self.consignorCB.addItem("Akash Enterprises")
        self.consignorCB.addItem("Preet Company")

        self.consigneeLabel = QLabel("&Consignee", self)
        self.consigneeLabel.setFont(font)
        self.consigneeLabel.setObjectName("consigneeLabel")
        self.consigneeCB = QComboBox(self)
        self.consigneeCB.setObjectName("consigneeCB")
        self.consigneeLabel.setBuddy(self.consigneeCB)
        self.consigneeCB.addItem("Akash Enterprises")
        self.consigneeCB.addItem("Preet Company")

        self.snoLabel = QLabel("&S. No.", self)
        self.snoLabel.setFont(font)
        self.snoLabel.setObjectName("snoLabel")
        self.snoText = QTextEdit(self)
        self.snoText.setObjectName("snoText")
        self.snoText.setMaximumHeight(25)
        self.snoLabel.setBuddy(self.snoText)

        self.dateLabel = QLabel("&Date", self)
        self.dateLabel.setFont(font)
        self.dateLabel.setObjectName("dateLabel")
        self.dateEdit = QDateEdit(self)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.dateLabel.setBuddy(self.dateEdit)

        self.itemDescriptionLabel = QLabel("Item Descrition", self)
        self.itemDescriptionLabel.setObjectName("itemDescriptionLabel")

        self.itemDescriptionLineEdit = QLineEdit(self)
        self.itemDescriptionLineEdit.setObjectName("itemDescriptionLineEdit")

        self.packingLabel = QLabel("Packing", self)
        self.packingLabel.setObjectName("packingLabel")

        self.packingLineEdit = QLineEdit(self)
        self.packingLineEdit.setObjectName("packingLineEdit")
        self.packingLineEdit.setValidator(QIntValidator())

        self.packagesLabel = QLabel("Packages", self)
        self.packagesLabel.setObjectName("packagesLabel")

        self.packagesLineEdit = QLineEdit(self)
        self.packagesLineEdit.setObjectName("packagesLineEdit")
        self.packagesLineEdit.setValidator(QIntValidator())

        self.weightLabel = QLabel("Weight", self)
        self.weightLabel.setObjectName("weightLabel")

        self.weightLineEdit = QLineEdit(self)
        self.weightLineEdit.setObjectName("weightLineEdit")
        self.weightLineEdit.setValidator(QIntValidator())

        self.addItemPushBut = QPushButton("Add Item", self)
        self.addItemPushBut.clicked.connect(lambda: self.addItemclicked())

        self.gridLayout.addWidget(self.fromLabel, 0, 0)
        self.gridLayout.addWidget(self.fromCB, 0, 1)
        self.gridLayout.addWidget(self.dateLabel, 0, 2)
        self.gridLayout.addWidget(self.dateEdit, 0, 3)
        self.gridLayout.addWidget(self.destLabel, 1, 0)
        self.gridLayout.addWidget(self.destCB, 1, 1)
        self.gridLayout.addWidget(self.snoLabel, 1, 2)
        self.gridLayout.addWidget(self.snoText, 1, 3)
        self.gridLayout.addWidget(self.consignorLabel, 2, 0)
        self.gridLayout.addWidget(self.consignorCB, 2, 1)
        self.gridLayout.addWidget(self.consigneeLabel, 3, 0)
        self.gridLayout.addWidget(self.consigneeCB, 3, 1)

        self.addItemGrid.addWidget(self.itemDescriptionLabel, 0, 0)
        self.addItemGrid.addWidget(self.itemDescriptionLineEdit, 0, 1)
        self.addItemGrid.addWidget(self.packingLabel, 0, 2)
        self.addItemGrid.addWidget(self.packingLineEdit, 0, 3)
        self.addItemGrid.addWidget(self.weightLabel, 0, 4)
        self.addItemGrid.addWidget(self.weightLineEdit, 0, 5)
        self.addItemGrid.addWidget(self.packagesLabel, 1, 2)
        self.addItemGrid.addWidget(self.packagesLineEdit, 1, 3)
        self.addItemGrid.addWidget(self.addItemPushBut, 1, 5)

        self.qvLayout.addLayout(self.gridLayout)
        self.qvLayout.addLayout(self.addItemGrid)
        self.qvLayout.addWidget(self.itemsTable)

        self.setLayout(self.qvLayout)
        QMetaObject.connectSlotsByName(self)

    def addItemclicked(self):
        a = self.itemDescriptionLineEdit.text()
        b = self.packingLineEdit.text()
        c = self.packagesLineEdit.text()
        d = self.weightLineEdit.text()
        self.itemsTable.appendRow([a, b, c, d])
        self.itemDescriptionLineEdit.clear()
        self.packagesLineEdit.clear()
        self.packingLineEdit.clear()
        self.weightLineEdit.clear()
