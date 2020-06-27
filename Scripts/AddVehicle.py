from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class AddVehicleform(QDialog):
    def __init__(self):
        super(AddVehicleform,self).__init__()
        self.resize(600, 200)
        self.setupUi()

    def setupUi(self):
        self.gridLayout = QGridLayout(self)
        self.setLayout(self.gridLayout)

        self.formLayout = QFormLayout()
        self.centralwidget = QWidget(self)
        font = QFont()
        font.setPointSize(12)


        self.vehicleNumLabel = QLabel('&Vehicle number: ',self)
        self.vehicleNumLabel.setFont(font)
        self.vehicleNumLineEdit = QLineEdit()
        self.vehicleNumLineEdit.setPlaceholderText("Example: MH12DE1433")
        self.vehicleNumLabel.setBuddy(self.vehicleNumLineEdit)
        self.vehicleNumLineEdit.textChanged.connect(self.checkVehicleNo)


        self.vehicleModelLabel = QLabel('&Vehicle model: ',self)
        self.vehicleModelLabel.setFont(font)
        self.vehicleModelLineEdit = QLineEdit()
        self.vehicleModelLabel.setBuddy(self.vehicleModelLineEdit)


        self.invalidVehicleNumLabel  = QLabel('*Invalid Vehicle Number',self)
        self.invalidVehicleNumLabel.setStyleSheet("QLabel{color:red;font-size:12px;}")
        self.invalidVehicleNumLabel.hide()

        
        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Reset | QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        self.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.saveClicked)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.close)
        # self.buttonBox.button(QDialogButtonBox.Reset).clicked.connect(self.clear)

        self.formLayout.addRow(self.vehicleNumLabel,self.vehicleNumLineEdit)
        self.formLayout.addRow(self.vehicleModelLabel,self.vehicleModelLineEdit)
        self.buttonBox.button(QDialogButtonBox.Reset).clicked.connect(self.vehicleNumLineEdit.clear)
        self.buttonBox.button(QDialogButtonBox.Reset).clicked.connect(self.vehicleModelLineEdit.clear)

        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

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

        if ( (len(veh_no) != 10) or (is_string == 0) ) or (is_no == 0) :
            self.invalidVehicleNumLabel.show()
            self.vehicleNumLineEdit.setStyleSheet("border:1px solid red")
        else :
            self.invalidVehicleNumLabel.hide()
            self.vehicleNumLineEdit.setStyleSheet("border:")


    def saveClicked(self):
        self.accept()
        print('YES')
 


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = AddVehicleform()
    ui.show()
    sys.exit(app.exec_())
