import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,QLabel
from PyQt5 import uic, QtCore

form_class = uic.loadUiType("mainfail.ui")[0]
class MainFailClass(QForm, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Wrong Button')

        self.show()


