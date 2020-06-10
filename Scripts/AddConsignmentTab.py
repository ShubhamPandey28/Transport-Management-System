from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class AddConsignmentForm(QGroupBox):
    def __init__(self, parent=None):
        super(AddConsignmentForm, self).__init__(parent)

        self.setObjectName("BillGenerationMainWindow")
        self.setMaximumSize(QSize(400, 300))
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
        self.resize(400, 300)
        self.setFont(font)

        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")

        self.fromLabel = QLabel("&From", self)
        self.fromLabel.setFont(font)
        self.fromLabel.setObjectName("fromLabel")
        self.fromCB = QComboBox(self)
        self.fromCB.setObjectName("fromCB")
        self.fromLabel.setBuddy(self.fromCB)
        self.fromCB.addItem("Kolkata-WB")
        self.fromCB.addItem("Meerut-UP")
        self.fromCB.addItem("Jaipur-Rajasthan")
        self.fromCB.addItem("Kota-Rajansthan")
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

        self.consignorLabel = QLabel("Consigne&r", self)
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

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.dateLabel)
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.dateEdit)
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.fromLabel)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.fromCB)
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.destLabel)
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.destCB)
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.consignorLabel)
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.consignorCB)
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.consigneeLabel)
        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.consigneeCB)
        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.snoLabel)
        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.snoText)

        self.gridLayout.addLayout(self.formLayout, 0, 0)

        QMetaObject.connectSlotsByName(self)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = AddConsignmentForm()
    ui.show()
    sys.exit(app.exec_())
