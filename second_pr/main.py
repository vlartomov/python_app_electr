from importlib.util import set_loader
import sys
from unittest import result
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from des import *
from cgitb import text
import requests
from bs4 import BeautifulSoup
import pandas as pd


class Handler(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self):
        url = "https://www.kinopoisk.ru/lists/movies/top250/"
        r = requests.get(url)
        r.text
        soup = BeautifulSoup(r.text, 'html.parser')
        ementa = getattr(soup.find('span', class_='styles_kinopoiskValuePositive__vOb2E styles_kinopoiskValue__9qXjg'), 'text', None)
        self.mysignal.emit(ementa)
      

class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start_handler)

        self.mythread = Handler()
        self.mythread.mysignal.connect(self.add_item)

    def start_handler(self):
        self.mythread.start()

    def add_item(self, value):
        self.ui.plainTextEdit.appendPlainText(value)

    def closeEvent(self, value):
        result = QtWidgets.QMessageBox.question(self, 'Оповещение', 'Close programm?',
                                                QtWidgets.QMessageBox.Yes |  QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.No:
            value.ignore()
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mywin = GUI()
    mywin.show()
    sys.exit(app.exec_())

