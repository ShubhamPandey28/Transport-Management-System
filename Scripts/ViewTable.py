from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from .itemsTableView import itemsTableView
from .server import get_table
from .dictionaries import *


class debugView(QDialog):
    def __init__(self, table_name):
        super(debugView, self).__init__()  # parent constructor
        self.setObjectName("View" + table_name)
        self.setWindowTitle("View " + table_name)

        self.table_name = table_name

        self.resize(500, 400)
        self.setupUi()

    def setupUi(self):
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        newLayout = QHBoxLayout(self)
        data = get_table(self.table_name)['result']

        tmp = {
            'Vehicle' : list(Vehicle_Dict().keys()),
            'Consignor_Consignee' : list(Consignor_Consignee_Dict().keys()),
            'Consignment' : list(Consignment_Dict().keys()),
            'Repair_Log' : list(Repair_Log_Dict().keys()),
            'Bills' : list(Bills_Dict().keys()),
        }

        headings = tmp[self.table_name]

        table = itemsTableView(headings, 0, len(headings))
        for row in data:
            table.appendRow(row)
    
        table.resizeColumnsToContents()

        newLayout.addWidget(table)

        self.setLayout(newLayout)

