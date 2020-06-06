# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddConsignor.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont



class Ui_AddConsignor(object):
    def setupUi(self, AddConsignor):
        AddConsignor.setObjectName("AddConsignor")
        AddConsignor.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(AddConsignor)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 631, 441))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        
        self.stateCityModel = QStandardItemModel()

        self.companyNameLabel = QtWidgets.QLabel(self.groupBox)
        self.companyNameLabel.setGeometry(QtCore.QRect(10, 40, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.companyNameLabel.setFont(font)
        self.companyNameLabel.setObjectName("companyNameLabel")
        self.cityLabel = QtWidgets.QLabel(self.groupBox)
        self.cityLabel.setGeometry(QtCore.QRect(10, 160, 51, 16))
        self.cityLabel.setObjectName("cityLabel")
        
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(140, 40, 351, 31))
        self.lineEdit.setObjectName("lineEdit")
        
        self.stateLabel = QtWidgets.QLabel(self.groupBox)
        self.stateLabel.setGeometry(QtCore.QRect(10, 106, 67, 21))
        self.stateLabel.setObjectName("stateLabel")
        
        self.stateComboBox = QtWidgets.QComboBox(self.groupBox)
        self.stateComboBox.setGeometry(QtCore.QRect(100, 100, 281, 31))
        self.stateComboBox.setObjectName("stateComboBox")
        self.stateComboBox.setModel(self.stateCityModel)

        
        self.cityComboBox = QtWidgets.QComboBox(self.groupBox)
        self.cityComboBox.setGeometry(QtCore.QRect(100, 150, 281, 31))
        self.cityComboBox.setObjectName("cityComboBox")
        self.cityComboBox.setModel(self.stateCityModel)


        data = {
    'Rajasthan': ['Kota', 'jaipur', 'Ajmer'],
    'Uttar Pradesh': ['Kanpur', 'Agra', 'Meerut'],
    'Gujarat': ['Ahmendabad', 'Gandhi Nagar', 'Surat']
            }
        
        for k, v in data.items():
            state = QStandardItem(k)
            self.stateCityModel.appendRow(state)
            for value in v:
                city = QStandardItem(value)
                state.appendRow(city)
        #until now both comboBoxes are showing states
        self.stateComboBox.currentIndexChanged.connect(self.updateCityComboBox)
        self.updateCityComboBox(0)
        
        self.addressLabel = QtWidgets.QLabel(self.groupBox)
        self.addressLabel.setGeometry(QtCore.QRect(10, 210, 67, 21))
        self.addressLabel.setObjectName("addressLabel")
        
        self.AddressLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.AddressLineEdit.setGeometry(QtCore.QRect(100, 204, 421, 31))
        self.AddressLineEdit.setObjectName("AddressLineEdit")
        
        self.gstLabel = QtWidgets.QLabel(self.groupBox)
        self.gstLabel.setGeometry(QtCore.QRect(10, 320, 67, 17))
        self.gstLabel.setObjectName("gstLabel")
        
        self.gstLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.gstLineEdit.setGeometry(QtCore.QRect(100, 310, 421, 31))
        self.gstLineEdit.setObjectName("gstLineEdit")
        
        self.addAsLabel = QtWidgets.QLabel(self.groupBox)
        self.addAsLabel.setGeometry(QtCore.QRect(10, 400, 67, 31))
        self.addAsLabel.setObjectName("addAsLabel")
        
        self.consignorRadioBut = QtWidgets.QRadioButton(self.groupBox)
        self.consignorRadioBut.setGeometry(QtCore.QRect(80, 400, 112, 31))
        self.consignorRadioBut.setObjectName("consignorRadioBut")
        self.consigneeRadioBut = QtWidgets.QRadioButton(self.groupBox)
        self.consigneeRadioBut.setGeometry(QtCore.QRect(210, 400, 112, 31))
        self.consigneeRadioBut.setObjectName("consigneeRadioBut")
        
        self.bothRadioBut = QtWidgets.QRadioButton(self.groupBox)
        self.bothRadioBut.setGeometry(QtCore.QRect(350, 400, 71, 31))
        self.bothRadioBut.setObjectName("bothRadioBut")
        
        self.pinCodeLabel = QtWidgets.QLabel(self.groupBox)
        self.pinCodeLabel.setGeometry(QtCore.QRect(10, 260, 67, 31))
        self.pinCodeLabel.setObjectName("pinCodeLabel")
        self.pinCodeLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.pinCodeLineEdit.setGeometry(QtCore.QRect(100, 260, 113, 31))
        self.pinCodeLineEdit.setObjectName("pinCodeLineEdit")
        
        self.mobNoLabel = QtWidgets.QLabel(self.groupBox)
        self.mobNoLabel.setGeometry(QtCore.QRect(10, 366, 81, 21))
        self.mobNoLabel.setObjectName("mobNoLabel")
        
        self.mobNoLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.mobNoLineEdit.setGeometry(QtCore.QRect(140, 360, 131, 31))
        self.mobNoLineEdit.setObjectName("mobNoLineEdit")
        
        self.nineOneLabel = QtWidgets.QLabel(self.groupBox)
        self.nineOneLabel.setGeometry(QtCore.QRect(100, 360, 41, 31))
        self.nineOneLabel.setObjectName("nineOneLabel")
        
        self.SavePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.SavePushButton.setGeometry(QtCore.QRect(70, 500, 89, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SavePushButton.setFont(font)
        self.SavePushButton.setObjectName("SavePushButton")
        
        self.cancelPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelPushButton.setGeometry(QtCore.QRect(180, 500, 89, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cancelPushButton.setFont(font)
        self.cancelPushButton.setObjectName("cancelPushButton")
        
        self.resetPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetPushButton.setGeometry(QtCore.QRect(290, 500, 89, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.resetPushButton.setFont(font)
        self.resetPushButton.setObjectName("resetPushButton")
        
        AddConsignor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddConsignor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFill = QtWidgets.QMenu(self.menubar)
        self.menuFill.setObjectName("menuFill")
        AddConsignor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddConsignor)
        self.statusbar.setObjectName("statusbar")
        AddConsignor.setStatusBar(self.statusbar)
        self.actionCreate_BIll = QtWidgets.QAction(AddConsignor)
        self.actionCreate_BIll.setObjectName("actionCreate_BIll")
        self.menuFill.addAction(self.actionCreate_BIll)
        self.menubar.addAction(self.menuFill.menuAction())

        self.retranslateUi(AddConsignor)
        QtCore.QMetaObject.connectSlotsByName(AddConsignor)

    def updateCityComboBox(self,index):
        #index(int row, int column, const QModelIndex &parent = QModelIndex()) const override
        indx = self.stateCityModel.index(index, 0, self.stateComboBox.rootModelIndex())   
        self.cityComboBox.setRootModelIndex(indx)
        self.cityComboBox.setCurrentIndex(0)
    
    
    def retranslateUi(self, AddConsignor):
        _translate = QtCore.QCoreApplication.translate
        AddConsignor.setWindowTitle(_translate("AddConsignor", "MainWindow"))
        self.companyNameLabel.setText(_translate("AddConsignor", "Company Name:"))
        self.cityLabel.setText(_translate("AddConsignor", "City:"))
        self.stateLabel.setText(_translate("AddConsignor", "State:"))
        self.addressLabel.setText(_translate("AddConsignor", "Address:"))
        self.gstLabel.setText(_translate("AddConsignor", "GSTIN:"))
        self.addAsLabel.setText(_translate("AddConsignor", "Add as:"))
        self.consignorRadioBut.setText(_translate("AddConsignor", "Consignor"))
        self.consigneeRadioBut.setText(_translate("AddConsignor", "Consignee"))
        self.bothRadioBut.setText(_translate("AddConsignor", "Both"))
        self.pinCodeLabel.setText(_translate("AddConsignor", "Pin Code:"))
        self.mobNoLabel.setText(_translate("AddConsignor", "Mobile No."))
        self.nineOneLabel.setText(_translate("AddConsignor", "+91-"))
        self.SavePushButton.setText(_translate("AddConsignor", "Save"))
        self.cancelPushButton.setText(_translate("AddConsignor", "Cancel"))
        self.resetPushButton.setText(_translate("AddConsignor", "Reset"))
        self.menuFill.setTitle(_translate("AddConsignor", "File"))
        self.actionCreate_BIll.setText(_translate("AddConsignor", "Create BIll"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddConsignor = QtWidgets.QMainWindow()
    ui = Ui_AddConsignor()
    ui.setupUi(AddConsignor)
    AddConsignor.show()
    sys.exit(app.exec_())
