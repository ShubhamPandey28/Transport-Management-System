# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 561, 361))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(110, 50, 311, 151))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.vehicalIDLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.vehicalIDLabel.setObjectName("vehicalIDLabel")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.vehicalIDLabel
        )
        self.vehicalIDLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.vehicalIDLineEdit.setObjectName("vehicalIDLineEdit")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.vehicalIDLineEdit
        )
        self.amountLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.amountLabel.setObjectName("amountLabel")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.amountLabel
        )
        self.amountLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.amountLineEdit.setObjectName("amountLineEdit")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.amountLineEdit
        )
        self.billNoLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.billNoLabel.setObjectName("billNoLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.billNoLabel)
        self.billNoLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.billNoLineEdit.setObjectName("billNoLineEdit")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.billNoLineEdit
        )
        self.billDateLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.billDateLabel.setObjectName("billDateLabel")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.billDateLabel
        )
        self.billDateLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.billDateLineEdit.setObjectName("billDateLineEdit")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.billDateLineEdit
        )
        self.partsLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.partsLabel.setObjectName("partsLabel")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.partsLabel
        )
        self.partsLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.partsLineEdit.setObjectName("partsLineEdit")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.partsLineEdit
        )
        self.addEntryButton = QtWidgets.QPushButton(self.tab)
        self.addEntryButton.setGeometry(QtCore.QRect(220, 240, 89, 25))
        self.addEntryButton.setObjectName("addEntryButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.vehicalIDLabel.setText(_translate("MainWindow", "Vehical ID"))
        self.amountLabel.setText(_translate("MainWindow", "Amount"))
        self.billNoLabel.setText(_translate("MainWindow", "Bill No."))
        self.billDateLabel.setText(_translate("MainWindow", "Bill Date"))
        self.partsLabel.setText(_translate("MainWindow", "Parts"))
        self.addEntryButton.setText(_translate("MainWindow", "Add Entry"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab), _translate("MainWindow", "New Entry")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "View History")
        )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
