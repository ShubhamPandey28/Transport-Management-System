from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class AddVehicleform(QDialog):
    def __init__(self):
        super(AddVehicleform,self).__init__()
        self.setObjectName("AddVehicleform")
        self.resize(600, 400)
        self.setupUi()

    def setupUi(self):
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName('formLayout')
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setGeometry(50,50,500,500)
        font = QFont()
        font.setPointSize(12)


        self.vehicleNumLabel = QLabel('&Vehicle number: ',self)
        self.vehicleNumLabel.setFont(font)
        self.vehicleNumLabel.setObjectName("vehicleNumLabel")
        self.vehicleNumLineEdit = QLineEdit()
        self.vehicleNumLineEdit.setGeometry(QRect(140, 40, 351, 31))
        self.vehicleNumLineEdit.setObjectName("vehicleNumLineEdit")
        self.vehicleNumLabel.setBuddy(self.vehicleNumLineEdit)
        self.vehicleNumLineEdit.textChanged.connect(self.checkVehicleNo)


        self.vehicleModelLabel = QLabel('&Vehicle model: ',self)
        self.vehicleModelLabel.setFont(font)
        self.vehicleModelLabel.setObjectName("vehicleModelLabel")
        self.vehicleModelLineEdit = QLineEdit()
        self.vehicleModelLineEdit.setGeometry(QRect(140, 40, 351, 31))
        self.vehicleModelLineEdit.setObjectName("vehicleModelLineEdit")
        self.vehicleModelLabel.setBuddy(self.vehicleModelLineEdit)


        self.invalidVehicleNumLabel  = QLabel('*Invalid Vehicle Number',self)
        self.invalidVehicleNumLabel.setObjectName('invalidvehicleNum')
        self.invalidVehicleNumLabel.setGeometry(QRect(400,150,200,100))
        self.invalidVehicleNumLabel.setStyleSheet("QLabel{color:red;font-size:12px;}")
        self.invalidVehicleNumLabel.hide()

        
        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Reset | QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        self.buttonBox.setGeometry(QRect(100,250,270,120))
        self.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.saveClicked)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.close)
        # self.buttonBox.button(QDialogButtonBox.Reset).clicked.connect(self.clear)

        self.formLayout.addRow(self.vehicleNumLabel,self.vehicleNumLineEdit)
        self.formLayout.addRow(self.vehicleModelLabel,self.vehicleModelLineEdit)
        self.buttonBox.button(QDialogButtonBox.Reset).clicked.connect(self.vehicleNumLineEdit.clear)
        self.buttonBox.button(QDialogButtonBox.Reset).clicked.connect(self.vehicleModelLineEdit.clear)




        self.centralwidget.setLayout(self.formLayout)
        QMetaObject.connectSlotsByName(self)


    def checkVehicleNo(self):
        veh_no=self.vehicleNumLineEdit.text()
        is_string=1
        for i in veh_no[:2]+veh_no[4:6]:
            is_string&=( 64<ord(i) and ord(i)<91 )
        

        is_no=1
        for i in veh_no[2:4]+veh_no[6:]:
            is_no&=( 47<ord(i) and ord(i)<58 )

        if ( (len(veh_no) is not 10) or (is_string is 0) ) or (is_no is 0) :
            self.invalidVehicleNumLabel.show()
            self.vehicleNumLineEdit.setStyleSheet("border:1px solid red")
        else :
            self.invalidVehicleNumLabel.hide()
            self.vehicleNumLineEdit.setStyleSheet("border:")


    def saveClicked(self):
        print('YES')
 


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = AddVehicleform()
    ui.show()
    sys.exit(app.exec_())
