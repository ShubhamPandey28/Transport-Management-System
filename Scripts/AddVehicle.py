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


        self.Vehicle_Num = QLabel('&Vehicle number: ',self)
        self.Vehicle_Num.setFont(font)
        self.Vehicle_Num.setObjectName("Vehicle_Num")
        self.Vehicle_NumLineEdit = QLineEdit()
        self.Vehicle_NumLineEdit.setGeometry(QRect(140, 40, 351, 31))
        self.Vehicle_NumLineEdit.setObjectName("Vehicle_NumLineEdit")
        self.Vehicle_Num.setBuddy(self.Vehicle_NumLineEdit)
        self.Vehicle_NumLineEdit.textChanged.connect(self.checkVehicleNo)


        self.Vehicle_Model = QLabel('&Vehicle model: ',self)
        self.Vehicle_Model.setFont(font)
        self.Vehicle_Model.setObjectName("Vehicle_Model")
        self.Vehicle_ModelLineEdit = QLineEdit()
        self.Vehicle_ModelLineEdit.setGeometry(QRect(140, 40, 351, 31))
        self.Vehicle_ModelLineEdit.setObjectName("Vehicle_ModelLineEdit")
        self.Vehicle_Model.setBuddy(self.Vehicle_ModelLineEdit)

        
        self.Current_loc = QLabel('&Current Location: ',self)
        self.Current_loc.setFont(font)
        self.Current_loc.setObjectName("Current_loc")
        self.Current_locLineEdit = QLineEdit()
        self.Current_locLineEdit.setGeometry(QRect(140, 40, 351, 31))
        self.Current_locLineEdit.setObjectName("Current_locLineEdit")
        self.Current_loc.setBuddy(self.Current_locLineEdit)


        self.Status = QLabel('&Status: ',self)
        self.Status.setFont(font)
        self.Status.setObjectName("Status")
        self.Statuscombobox = QComboBox()
        self.Statuscombobox.setObjectName("Statuscombobox")
        self.Statuscombobox.addItems(["Idle","Working","In repair","inoperable"])
        self.Status.setBuddy(self.Statuscombobox)

        self.invalidVehicle_Num  = QLabel('*Invalid Vehicle Number',self)
        self.invalidVehicle_Num.setObjectName('invalidVehicle_Num')
        self.invalidVehicle_Num.setGeometry(QRect(400,150,200,100))
        self.invalidVehicle_Num.setStyleSheet("QLabel{color:red;font-size:12px;}")
        self.invalidVehicle_Num.hide()

        
        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Reset | QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        self.buttonBox.setGeometry(QRect(100,250,270,120))
        self.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.saveClicked)

        self.formLayout.addRow(self.Vehicle_Num,self.Vehicle_NumLineEdit)
        self.formLayout.addRow(self.Vehicle_Model,self.Vehicle_ModelLineEdit)
        self.formLayout.addRow(self.Current_loc,self.Current_locLineEdit)
        self.formLayout.addRow(self.Status,self.Statuscombobox)


        self.centralwidget.setLayout(self.formLayout)
        QMetaObject.connectSlotsByName(self)


    def checkVehicleNo(self):
        veh_no=self.Vehicle_NumLineEdit.text()
        is_string=1
        for i in veh_no[:2]+veh_no[4:6]:
            is_string&=( 64<ord(i) and ord(i)<91 )
        

        is_no=1
        for i in veh_no[2:4]+veh_no[6:]:
            is_no&=( 47<ord(i) and ord(i)<58 )

        if ( (len(veh_no) is not 10) or (is_string is 0) ) or (is_no is 0) :
            self.invalidVehicle_Num.show()
            self.Vehicle_NumLineEdit.setStyleSheet("border:1px solid red")
        else :
            self.invalidVehicle_Num.hide()
            self.Vehicle_NumLineEdit.setStyleSheet("border:")


    def saveClicked(self):
        print('YES')
 


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = AddVehicleform()
    ui.show()
    sys.exit(app.exec_())
