from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class RepairForm(QGroupBox):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.setObjectName("Form")
        self.setMinimumSize(QSize(400, 250))
        self.setMaximumSize(QSize(400, 250))
        self.setObjectName("groupBox")

        self.setupUi()

    def setupUi(self):

        # Form Data
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.vehicalIDLabel = QLabel(self)
        self.vehicalIDLabel.setObjectName("vehicalIDLabel")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.vehicalIDLabel)
        self.vehicalIDLineEdit = QLineEdit(self)
        self.vehicalIDLineEdit.setObjectName("vehicalIDLineEdit")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.vehicalIDLineEdit)
        self.amountLabel = QLabel(self)
        self.amountLabel.setObjectName("amountLabel")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.amountLabel)
        self.amountLineEdit = QLineEdit(self)
        self.amountLineEdit.setObjectName("amountLineEdit")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.amountLineEdit)
        self.billNoLabel = QLabel(self)
        self.billNoLabel.setObjectName("billNoLabel")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.billNoLabel)
        self.billNoLineEdit = QLineEdit(self)
        self.billNoLineEdit.setObjectName("billNoLineEdit")
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.billNoLineEdit)
        self.billDateLabel = QLabel(self)
        self.billDateLabel.setObjectName("billDateLabel")
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.billDateLabel)
        self.billDateLineEdit = QLineEdit(self)
        self.billDateLineEdit.setObjectName("billDateLineEdit")
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.billDateLineEdit)
        self.partsLabel = QLabel(self)
        self.partsLabel.setObjectName("partsLabel")
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.partsLabel)
        self.partsLineEdit = QLineEdit(self)
        self.partsLineEdit.setObjectName("partsLineEdit")
        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.partsLineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.addEntryButton = QPushButton(self)
        self.addEntryButton.setObjectName("addEntryButton")
        self.verticalLayout.addWidget(self.addEntryButton)

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.setTitle(_translate("Form", "GroupBox"))
        self.vehicalIDLabel.setText(_translate("Form", "Vehical ID"))
        self.amountLabel.setText(_translate("Form", "Amount"))
        self.billNoLabel.setText(_translate("Form", "Bill No."))
        self.billDateLabel.setText(_translate("Form", "Bill Date"))
        self.partsLabel.setText(_translate("Form", "Parts"))
        self.addEntryButton.setText(_translate("Form", "Add Entry"))
