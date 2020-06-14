from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sys

data = {
    "col1": ["1", "2", "3", "4"],
    "col2": ["1", "2", "1", "3"],
    "col3": ["1", "1", "2", "1"],
}


class itemsTableView(QTableWidget):
    def __init__(self, headings, *args):
        QTableWidget.__init__(self, *args)
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.headings = headings
        self.setHorizontalHeaderLabels(self.headings)

        for i in range(len(headings)):
            self.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)

        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def appendRow(self, rowData):
        self.rowNumber = self.rowCount()
        self.insertRow(self.rowNumber)
        data = [QTableWidgetItem(x) for x in rowData]
        for i in range(len(self.headings)):
            self.setItem(self.rowNumber, i, data[i])


def main(args):
    app = QApplication(args)
    headings = ["Description", "Packing"]
    table = itemsTableView(headings, 0, len(headings))
    table.appendRow(["jkfbs", "45"])
    table.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main(sys.argv)
