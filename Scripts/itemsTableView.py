import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *


class itemsTableView(QTableWidget):
    def __init__(self, headings, *args):
        QTableWidget.__init__(self, *args)
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.headings = headings
        self.setHorizontalHeaderLabels(self.headings)

        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def appendRow(self, rowData):
        self.rowNumber = self.rowCount()
        self.insertRow(self.rowNumber)
        data = [QTableWidgetItem(str(x)) for x in rowData]
        for i in range(len(self.headings)):
            self.setItem(self.rowNumber, i, data[i])

    def setToStretch():

        for i in range(len(self.headings)):
            self.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)
