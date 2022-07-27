#import imp
#from readline import append_history_file
from importlib.util import set_loader
import sys
import time
from unittest import result
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from dest import *

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.handler)
        self.ui.pushButton_2.clicked.connect(self.setcolor)

    def handler(self):
        self.ui.pushButton.setDisabled(True)
        self.ui.plainTextEdit.appendPlainText('text')
        self.ui.label.setText('text2')

    def setcolor(self):
        self.ui.pushButton.setText("111111")
        self.ui.pushButton.setStyleSheet('background-color: red; white;')
        self.ui.pushButton.setDisabled(False)

    def closeEvent(self, value):
        result = QtWidgets.QMessageBox.question(self, 'Оповещение', 'Close programm?',
                                                QtWidgets.QMessageBox.Yes |  QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.No:
            value.ignore()
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())


   