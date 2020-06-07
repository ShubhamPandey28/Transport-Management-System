# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddConsignor.ui'



from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Ui_AddConsignor(QDialog):
    def __init__(self):
        super(Ui_AddConsignor,self).__init__()     #parent constructor
        self.setupUi()
        self.setObjectName("AddConsignor")
        self.resize(800, 600)
    def setupUi(self):
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QRect(0, 0, 631, 441))
        font = QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        
        self.stateCityModel = QStandardItemModel()

        self.companyNameLabel = QLabel(self.groupBox)
        self.companyNameLabel.setGeometry(QRect(10, 40, 121, 31))
        font = QFont()
        font.setPointSize(12)
        self.companyNameLabel.setFont(font)
        self.companyNameLabel.setObjectName("companyNameLabel")
        self.cityLabel = QLabel(self.groupBox)
        self.cityLabel.setGeometry(QRect(10, 160, 51, 16))
        self.cityLabel.setObjectName("cityLabel")
        
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QRect(140, 40, 351, 31))
        self.lineEdit.setObjectName("lineEdit")
        
        self.stateLabel = QLabel(self.groupBox)
        self.stateLabel.setGeometry(QRect(10, 106, 67, 21))
        self.stateLabel.setObjectName("stateLabel")
        
        self.stateComboBox = QComboBox(self.groupBox)
        self.stateComboBox.setGeometry(QRect(100, 100, 281, 31))
        self.stateComboBox.setObjectName("stateComboBox")
        self.stateComboBox.setModel(self.stateCityModel)

        
        self.cityComboBox = QComboBox(self.groupBox)
        self.cityComboBox.setGeometry(QRect(100, 150, 281, 31))
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
        
        self.addressLabel = QLabel(self.groupBox)
        self.addressLabel.setGeometry(QRect(10, 210, 67, 21))
        self.addressLabel.setObjectName("addressLabel")
        
        self.AddressLineEdit = QLineEdit(self.groupBox)
        self.AddressLineEdit.setGeometry(QRect(100, 204, 421, 31))
        self.AddressLineEdit.setObjectName("AddressLineEdit")
        
        self.gstLabel = QLabel(self.groupBox)
        self.gstLabel.setGeometry(QRect(10, 320, 67, 17))
        self.gstLabel.setObjectName("gstLabel")
        
        self.gstLineEdit = QLineEdit(self.groupBox)
        self.gstLineEdit.setGeometry(QRect(100, 310, 421, 31))
        self.gstLineEdit.setObjectName("gstLineEdit")
        
        self.addAsLabel = QLabel(self.groupBox)
        self.addAsLabel.setGeometry(QRect(10, 400, 67, 31))
        self.addAsLabel.setObjectName("addAsLabel")
        
        self.consignorRadioBut = QRadioButton(self.groupBox)
        self.consignorRadioBut.setGeometry(QRect(80, 400, 112, 31))
        self.consignorRadioBut.setObjectName("consignorRadioBut")
        self.consigneeRadioBut = QRadioButton(self.groupBox)
        self.consigneeRadioBut.setGeometry(QRect(210, 400, 112, 31))
        self.consigneeRadioBut.setObjectName("consigneeRadioBut")
        
        self.bothRadioBut = QRadioButton(self.groupBox)
        self.bothRadioBut.setGeometry(QRect(350, 400, 71, 31))
        self.bothRadioBut.setObjectName("bothRadioBut")
        
        self.pinCodeLabel = QLabel(self.groupBox)
        self.pinCodeLabel.setGeometry(QRect(10, 260, 67, 31))
        self.pinCodeLabel.setObjectName("pinCodeLabel")
        self.pinCodeLineEdit = QLineEdit(self.groupBox)
        self.pinCodeLineEdit.setGeometry(QRect(100, 260, 113, 31))
        self.pinCodeLineEdit.setObjectName("pinCodeLineEdit")
        
        self.mobNoLabel = QLabel(self.groupBox)
        self.mobNoLabel.setGeometry(QRect(10, 366, 81, 21))
        self.mobNoLabel.setObjectName("mobNoLabel")
        
        self.mobNoLineEdit = QLineEdit(self.groupBox)
        self.mobNoLineEdit.setGeometry(QRect(140, 360, 131, 31))
        self.mobNoLineEdit.setObjectName("mobNoLineEdit")
        
        self.nineOneLabel = QLabel(self.groupBox)
        self.nineOneLabel.setGeometry(QRect(100, 360, 41, 31))
        self.nineOneLabel.setObjectName("nineOneLabel")
        
        self.SavePushButton = QPushButton(self.centralwidget)
        self.SavePushButton.setGeometry(QRect(70, 500, 89, 31))
        font = QFont()
        font.setPointSize(14)
        self.SavePushButton.setFont(font)
        self.SavePushButton.setObjectName("SavePushButton")
        
        self.cancelPushButton = QPushButton(self.centralwidget)
        self.cancelPushButton.setGeometry(QRect(180, 500, 89, 31))
        font = QFont()
        font.setPointSize(14)
        self.cancelPushButton.setFont(font)
        self.cancelPushButton.setObjectName("cancelPushButton")
        
        self.resetPushButton = QPushButton(self.centralwidget)
        self.resetPushButton.setGeometry(QRect(290, 500, 89, 31))
        font = QFont()
        font.setPointSize(14)
        self.resetPushButton.setFont(font)
        self.resetPushButton.setObjectName("resetPushButton")
        
        
        self.retranslateUi(self)
        QMetaObject.connectSlotsByName(self)

    def updateCityComboBox(self,index):
        #index(int row, int column, const QModelIndex &parent = QModelIndex()) const override
        indx = self.stateCityModel.index(index, 0, self.stateComboBox.rootModelIndex())   
        self.cityComboBox.setRootModelIndex(indx)
        self.cityComboBox.setCurrentIndex(0)
    
    
    def retranslateUi(self, AddConsignor):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("AddConsignor", "MainWindow"))
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
        


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Ui_AddConsignor()
    ui.show()
    sys.exit(app.exec_())
