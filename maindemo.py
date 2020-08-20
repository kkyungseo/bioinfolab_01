import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QGraphicsView, QLabel, QMenuBar, QMenu, QStatusBar, QAction, qApp, QMessageBox
from PyQt5 import uic, QtCore
from mainfail import MainFailClass
form_class = uic.loadUiType("maindemo.ui")[0]

class MainWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Qomics')

        self.btn_survival.setToolTip('Survival Analysis')
        self.btn_drug.setToolTip('Drug Analysis')
        self.btn_CRISPR.setToolTip('CRISPR Analysis')
        self.btn_cellline.setToolTip('Cell Line')

        self.btn_survival.clicked.connect(self.open_SurvivalMainWindow)
        self.btn_drug.clicked.connect(self.open_DrugWindow)
        self.btn_CRISPR.clicked.connect(self.open_sgRNAWindow)
        self.btn_cellline.clicked.connect(self.open_CellLineWindow)

        actionExit = QAction('&Exit', self)
        actionExit.setShortcut('Ctrl+Q')
        actionExit.setStatusTip('Exit Application')
        actionExit.triggered.connect(qApp.quit)

        self.statusBar().showMessage('abcd')

        self.setGeometry(200, 100, 800, 530)

        self.show()

    def openSurvivalMainWindow(self):
        try:
            open_SurvivalMainWindow = SurvivalMainWindow()
            open_SurvivalMainWindow.show()
        except:
            open_fail + MainFailClass()
            open_fail.show()

    def openDrugWindow(self):
        try:
            open_DrugWindow = DrugWindow()
            open_DrugWindow.show()
        except:
            open_fail = MainFailClass()
            open_fail.show()

    def opensgRNAWindow(self):
        try:
            open_sgRNAWindow = sgRNAWindow()
            open_sgRNAWindow.show()
        except:
            open_fail = MainFailClass()
            open_fail.show()

    def openCellLineWindow(self):
        try:
            open_CellLineWindow = scatterWindow()
            open_CellLineWindow.show()
        except:
            open_fail = MainFailClass()
            open_fail.show()
