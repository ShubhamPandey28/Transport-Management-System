# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BillGenerateMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BillGenerationMainWindow(object):
    def setupUi(self, BillGenerationMainWindow):
        BillGenerationMainWindow.setObjectName("BillGenerationMainWindow")
        BillGenerationMainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(BillGenerationMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 771, 281))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.fromLabel = QtWidgets.QLabel(self.groupBox)
        self.fromLabel.setGeometry(QtCore.QRect(20, 40, 67, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fromLabel.setFont(font)
        self.fromLabel.setObjectName("fromLabel")
        self.destLabel = QtWidgets.QLabel(self.groupBox)
        self.destLabel.setGeometry(QtCore.QRect(20, 80, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.destLabel.setFont(font)
        self.destLabel.setObjectName("destLabel")
        self.consignorLabel = QtWidgets.QLabel(self.groupBox)
        self.consignorLabel.setGeometry(QtCore.QRect(20, 120, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.consignorLabel.setFont(font)
        self.consignorLabel.setObjectName("consignorLabel")
        self.consigneeLabel = QtWidgets.QLabel(self.groupBox)
        self.consigneeLabel.setGeometry(QtCore.QRect(20, 160, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.consigneeLabel.setFont(font)
        self.consigneeLabel.setObjectName("consigneeLabel")
        self.snoLabel = QtWidgets.QLabel(self.groupBox)
        self.snoLabel.setGeometry(QtCore.QRect(590, 90, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.snoLabel.setFont(font)
        self.snoLabel.setObjectName("snoLabel")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setGeometry(QtCore.QRect(590, 40, 110, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.consignorCB = QtWidgets.QComboBox(self.groupBox)
        self.consignorCB.setGeometry(QtCore.QRect(110, 120, 341, 21))
        self.consignorCB.setObjectName("consignorCB")
        self.consignorCB.addItem("")
        self.consignorCB.addItem("")
        self.destCB = QtWidgets.QComboBox(self.groupBox)
        self.destCB.setGeometry(QtCore.QRect(90, 79, 151, 21))
        self.destCB.setObjectName("destCB")
        self.destCB.addItem("")
        self.destCB.addItem("")
        self.destCB.addItem("")
        self.destCB.addItem("")
        self.fromCB = QtWidgets.QComboBox(self.groupBox)
        self.fromCB.setGeometry(QtCore.QRect(90, 40, 151, 21))
        self.fromCB.setObjectName("fromCB")
        self.fromCB.addItem("")
        self.fromCB.addItem("")
        self.fromCB.addItem("")
        self.fromCB.addItem("")
        self.fromCB.addItem("")
        self.consigneeCB = QtWidgets.QComboBox(self.groupBox)
        self.consigneeCB.setGeometry(QtCore.QRect(110, 160, 341, 21))
        self.consigneeCB.setObjectName("consigneeCB")
        self.consigneeCB.addItem("")
        self.consigneeCB.addItem("")
        self.snoText = QtWidgets.QTextEdit(self.groupBox)
        self.snoText.setGeometry(QtCore.QRect(650, 90, 104, 21))
        self.snoText.setObjectName("snoText")
        
        BillGenerationMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BillGenerationMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        BillGenerationMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BillGenerationMainWindow)
        self.statusbar.setObjectName("statusbar")
        BillGenerationMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(BillGenerationMainWindow)
        QtCore.QMetaObject.connectSlotsByName(BillGenerationMainWindow)

    def retranslateUi(self, BillGenerationMainWindow):
        _translate = QtCore.QCoreApplication.translate
        BillGenerationMainWindow.setWindowTitle(_translate("BillGenerationMainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("BillGenerationMainWindow", "GroupBox"))
        
        self.fromLabel.setText(_translate("BillGenerationMainWindow", "FROM:"))
        self.destLabel.setText(_translate("BillGenerationMainWindow", "DEST:"))
        self.consignorLabel.setText(_translate("BillGenerationMainWindow", "Consignor:"))
        self.consigneeLabel.setText(_translate("BillGenerationMainWindow", "Consignee:"))
        self.snoLabel.setText(_translate("BillGenerationMainWindow", "S.No."))
        
        self.consignorCB.setItemText(0, _translate("BillGenerationMainWindow", "Akash Enterprises"))
        self.consignorCB.setItemText(1, _translate("BillGenerationMainWindow", "Preet Company"))
        
        self.destCB.setItemText(0, _translate("BillGenerationMainWindow", "Kota-Rajansthan"))
        self.destCB.setItemText(1, _translate("BillGenerationMainWindow", "Meerut-UP"))
        self.destCB.setItemText(2, _translate("BillGenerationMainWindow", "Jaipur-Rajasthan"))
        self.destCB.setItemText(3, _translate("BillGenerationMainWindow", "Ahmedabad-Gujarat"))
        
        self.fromCB.setItemText(0, _translate("BillGenerationMainWindow", "Kolkata-WB"))
        self.fromCB.setItemText(1, _translate("BillGenerationMainWindow", "Meerut-UP"))
        self.fromCB.setItemText(2, _translate("BillGenerationMainWindow", "Jaipur-Rajasthan"))
        self.fromCB.setItemText(3, _translate("BillGenerationMainWindow", "Kota-Rajansthan"))
        self.fromCB.setItemText(4, _translate("BillGenerationMainWindow", "Ahmedabad-Gujarat"))
        
        self.consigneeCB.setItemText(0, _translate("BillGenerationMainWindow", "Akash Enterprises"))
        self.consigneeCB.setItemText(1, _translate("BillGenerationMainWindow", "Preet Company"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BillGenerationMainWindow = QtWidgets.QMainWindow()
    ui = Ui_BillGenerationMainWindow()
    ui.setupUi(BillGenerationMainWindow)
    BillGenerationMainWindow.show()
    sys.exit(app.exec_())