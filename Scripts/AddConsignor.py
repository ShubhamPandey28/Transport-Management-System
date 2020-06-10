# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddConsignor.ui'



from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Ui_AddConsignorDlg(QDialog):
    def __init__(self):
        super(Ui_AddConsignorDlg,self).__init__()     #parent constructor
        self.setObjectName("AddConsignorDlg")
        self.resize(800, 600)
        self.setupUi()

    def setupUi(self):
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName('formLayout')
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setGeometry(50,50,500,500)
        font = QFont()
        font.setPointSize(12)
        
        self.stateCityModel = QStandardItemModel()

        self.companyNameLabel = QLabel('&Company Name: ',self)
        self.companyNameLabel.setFont(font)
        self.companyNameLabel.setObjectName("companyNameLabel")
        self.companyNameLineEdit = QLineEdit()
        self.companyNameLineEdit.setGeometry(QRect(140, 40, 351, 31))
        self.companyNameLineEdit.setObjectName("companyNameLineEdit")
        self.companyNameLabel.setBuddy(self.companyNameLineEdit)
        
        self.stateLabel = QLabel('State: ',self)
        self.stateLabel.setObjectName("stateLabel")
        self.stateComboBox = QComboBox(self)
        self.stateComboBox.setObjectName("stateComboBox")
        self.stateComboBox.setModel(self.stateCityModel)
        self.stateLabel.setBuddy(self.stateComboBox)

        self.cityLabel = QLabel('City: ',self)
        self.cityLabel.setObjectName("cityLabel")
        self.cityComboBox = QComboBox(self)
        self.cityComboBox.setObjectName("cityComboBox")
        self.cityComboBox.setModel(self.stateCityModel)
        self.cityLabel.setBuddy(self.cityComboBox)


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
        
        self.addressLabel = QLabel('&Address',self)
        self.addressLabel.setObjectName("addressLabel")
        self.addressLineEdit = QLineEdit(self)
        self.addressLineEdit.setObjectName("addressLineEdit")
        self.addressLabel.setBuddy(self.addressLineEdit)

        
        self.gstLabel = QLabel('GSTINV: ',self)
        self.gstLabel.setObjectName("&gstLabel")
        self.gstLineEdit = QLineEdit(self)
        self.gstLineEdit.setObjectName("gstLineEdit")
        self.gstLabel.setBuddy(self.gstLineEdit)


        self.pinCodeLabel = QLabel('&Pin Code:',self)
        self.pinCodeLabel.setObjectName('pinCodeLabel')
        self.pinCodeLineEdit = QLineEdit(self)
        self.pinCodeLineEdit.setObjectName("pinCodeLineEdit")
        self.pinCodeLabel.setBuddy(self.pinCodeLineEdit)
        self.pinCodeLineEdit.setValidator(QIntValidator())
        self.pinCodeLineEdit.setMaxLength(6)
        self.pinCodeLineEdit.textChanged.connect(self.checkPin)

        
        self.mobNoLabel = QLabel('&Mobile No.',self)
        self.mobNoLabel.setObjectName("mobNoLabel")
        self.mobNoLineEdit = QLineEdit(self)
        self.mobNoLineEdit.setObjectName("mobNoLineEdit")
        self.mobNoLabel.setBuddy(self.mobNoLineEdit)
        self.mobNoLineEdit.setValidator(QIntValidator())
        self.mobNoLineEdit.setMaxLength(10)
        self.mobNoLineEdit.textChanged.connect(self.checkMobNo)

        self.invalidMobNoLabel  = QLabel('*Invalid Mobile Number',self)
        self.invalidMobNoLabel.setObjectName('invalidMobNoLabel')
        self.invalidMobNoLabel.setGeometry(QRect(550,201,200,100))
        self.invalidMobNoLabel.setStyleSheet("QLabel{color:red;font-size:12px;}")
        self.invalidMobNoLabel.hide()
        self.invalidPinLabel  = QLabel("*Invalid Pin Code",self)
        self.invalidPinLabel.setObjectName('invalidPinLabel')
        self.invalidPinLabel.setGeometry(QRect(550,177,200,100))
        self.invalidPinLabel.setStyleSheet("QLabel{color:red;font-size:12px;}")
        self.invalidPinLabel.hide()

            
        self.addAsLabel = QLabel(self)
        self.addAsLabel.setObjectName("addAsLabel")
        self.radioButGroupBox = QGroupBox(self)
        self.radioButGroupBox.setObjectName('radioButGroupBox')
        self.radioButGroupBox.setGeometry(QRect(200,200,500,500))
        # self.consignorRadioBut = QRadioButton('Consignor ',self.radioButGroupBox)
        # self.consignorRadioBut.setObjectName("consignorRadioBut")
        
        self.consigneeRadioBut = QRadioButton('Consignee ',self.radioButGroupBox)
        #self.consigneeRadioBut.setGeometry(QRect(200, 250, 270, 270))
        self.consigneeRadioBut.setObjectName("consigneeRadioBut")
        
        self.bothRadioBut = QRadioButton('Both ',self.radioButGroupBox)
        self.bothRadioBut.setGeometry(QRect(200, 250, 270, 270))
        self.bothRadioBut.setObjectName("bothRadioBut")
        self.addAsLabel.setBuddy(self.radioButGroupBox)
        
        

        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Reset | QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        self.buttonBox.setGeometry(QRect(100,250,270,120))
        self.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.saveClicked)

        
        
        self.formLayout.addRow(self.companyNameLabel,self.companyNameLineEdit)
        self.formLayout.addRow(self.stateLabel,self.stateComboBox)
        self.formLayout.addRow(self.cityLabel,self.cityComboBox)
        self.formLayout.addRow(self.addressLabel,self.addressLineEdit)
        self.formLayout.addRow(self.gstLabel,self.gstLineEdit)
        self.formLayout.addRow(self.pinCodeLabel,self.pinCodeLineEdit)
        self.formLayout.addRow(self.mobNoLabel,self.mobNoLineEdit)
        self.formLayout.addRow(self.addAsLabel,self.radioButGroupBox)

        self.centralwidget.setLayout(self.formLayout)
        QMetaObject.connectSlotsByName(self)

    def updateCityComboBox(self,index):
        #index(int row, int column, const QModelIndex &parent = QModelIndex()) const override
        indx = self.stateCityModel.index(index, 0, self.stateComboBox.rootModelIndex())   
        self.cityComboBox.setRootModelIndex(indx)
        self.cityComboBox.setCurrentIndex(0)
    def saveClicked(self):
        print(self.mobNoLineEdit.text())
        print('YES')
    def checkMobNo(self):
        if len(self.mobNoLineEdit.text())<10:
            self.invalidMobNoLabel.show()
            self.mobNoLineEdit.setStyleSheet("border:1px solid red")

        else:
            self.invalidMobNoLabel.hide()
            self.mobNoLineEdit.setStyleSheet("border:")

    def checkPin(self):
        if len(self.pinCodeLineEdit.text())<6:
            self.invalidPinLabel.show()
            self.pinCodeLineEdit.setStyleSheet("border:1px solid red")
        else:
            self.invalidPinLabel.hide()
            self.pinCodeLineEdit.setStyleSheet("border:")




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Ui_AddConsignorDlg()
    ui.show()
    sys.exit(app.exec_())