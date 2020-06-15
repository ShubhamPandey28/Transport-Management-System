from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class RepairForm(QGroupBox):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.setMinimumSize(QSize(400, 250))
        self.setMaximumSize(QSize(400, 250))
        self.setObjectName("groupBox")
        self.setWindowTitle("Repair Form")

        self.setupUi()

    def setupUi(self):

        # Form Data
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")

        self.vehicalIDLabel = QLabel("&Vehical ID", self)
        self.vehicalIDLabel.setObjectName("vehicalIDLabel")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.vehicalIDLabel)
        self.vehicalIDLineEdit = QLineEdit(self)
        self.vehicalIDLineEdit.setObjectName("vehicalIDLineEdit")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.vehicalIDLineEdit)
        self.vehicalIDLabel.setBuddy(self.vehicalIDLineEdit)

        self.amountLabel = QLabel("&Amount", self)
        self.amountLabel.setObjectName("amountLabel")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.amountLabel)
        self.amountLineEdit = QLineEdit(self)
        self.amountLineEdit.setObjectName("amountLineEdit")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.amountLineEdit)
        self.amountLabel.setBuddy(self.amountLineEdit)

        self.billNoLabel = QLabel("&Bill No.", self)
        self.billNoLabel.setObjectName("billNoLabel")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.billNoLabel)
        self.billNoLineEdit = QLineEdit(self)
        self.billNoLineEdit.setObjectName("billNoLineEdit")
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.billNoLineEdit)
        self.billNoLabel.setBuddy(self.billNoLineEdit)

        self.billDateLabel = QLabel("&Date", self)
        self.billDateLabel.setObjectName("billDateLabel")
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.billDateLabel)
        self.billDateLineEdit = QLineEdit(self)
        self.billDateLineEdit.setObjectName("billDateLineEdit")
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.billDateLineEdit)
        self.billDateLabel.setBuddy(self.billDateLineEdit)

        self.partsLabel = QLabel("&Part", self)
        self.partsLabel.setObjectName("partsLabel")
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.partsLabel)
        self.partsLineEdit = QLineEdit(self)
        self.partsLineEdit.setObjectName("partsLineEdit")
        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.partsLineEdit)
        self.partsLabel.setBuddy(self.partsLineEdit)

        self.verticalLayout.addLayout(self.formLayout)
        self.addEntryButton = QPushButton("Add Entry", self)
        self.addEntryButton.setObjectName("addEntryButton")
        self.verticalLayout.addWidget(self.addEntryButton)
