import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QGraphicsView, QLabel, QMenuBar, QMenu, QStatusBar, QAction, qApp
from PyQt5 import uic, QtCore

form_class = uic.loadUiType("maindemo.ui")[0]
class OpeningWindow(QMainWindow, form_class):

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

        ### exit function of menubar menuExit
        actionExit = QAction('&Exit', self)
        actionExit.setShortcut('Ctrl+Q')
        actionExit.setStatusTip('Exit Application')
        actionExit.triggered.connect(qApp.quit)

        self.statusBar().showMessage('abcd')

        self.setGeometry(200, 100, 800, 530)

        self.show()

    def openSurvivalMainWindow():
        openSurvivalMainWindow = SurvivalMainWindow()
        openSurvivalMainWindow.show()

    def openDrugWindow(self):
        openDrugWindow = DrugWindow()
        openDrugWindow.show()

    def opensgRNAWindow(self):
        opensgRNAWindow = sgRNAWindow()
        opensgRNAWindow.show()

    def openCellLineWindow(self):
        open_cellLineWindow = scatterWindow()
        open_cellLineWindow.show()


        if openSurvivalMainWindow():#survival window가 눌렀을 때는 열리게 하고
        
        else:
            #mainfail창을 보여주라!
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
