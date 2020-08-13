import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, qApp

class Exam(QWidget):
    def __init__(self):
        super().__init__() #QWidget에 대한 상위객체 생성
        self.initUI()
    def initUI(self):

        btn = QPushButton('asdcev', self) #버튼 안에 들어가는 문장 , 나 자신한테 버튼을 추가하겠다는 의미
        btn.resize(btn.sizeHint()) #버튼 크기 조절 내용
        btn.move(20, 30) #버튼의 위치 이동(왼쪽으로부터, 위쪽으로부터)
        btn.setToolTip('툴팁입니다' <b> 안녕하세요. </b>)
        #마우스를 대었을 때 나오는 메시지 지정, html 처럼 태그 지정 가능

        self.setGeometry(300,300,400,500) #창 크기를 조절하는 Geometry
        self.setWindowTitle('첫 번쨰 학습')
        self.show()

        #여기까지가 기본적인 설정

app = QAppication(sys.argv)
#application에 대한 오브젝트(객체) 생성, 명령에 대한 제어를 함
w = Exam()
sys.exit(app.exec_())
#프로그램을 종료하는 부분, 메인부분이 실행될  돌아가고 있다가 메인 루프가 끝나면 exit가 실행됨



############# 이벤트 처리, 메시지 박스
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
#필요한 기능의 이름을 적어서 추가하면 됨from PyQt5.QtCore import QCoreApplication

class Exam(QWidget):
    def __init__(self):
        super().__init__() #QWidget에 대한 상위객체 생성
        self.initUI()
    def initUI(self):
        btn = QPushButton("push me!", self)
        btn.resize(btn.sizeHint())
        btn.move(50,50) #여기 세 줄까지는 기본적인 디자인
        btn.clicked.connect(QCoreApplication.instance().quit)
        #instance로 객체를 부른 다음에 메소드를 불러옴, 객체가 나가지는 거니까 프로그램 종료
        #이 마지막 줄이 이벤트 처리

        self.resize(500,500)
        self.setWindowTitle("두 번쨰 시간")
        self.show()

    def closeEvent(self, QCloseEvent):
        ans = QMessageBox.question(self, "종료확인", "종료하시겠습니까?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        #No라는 상수를 함수에 넣어 실행
        #ans로 종료 여부 결정

        if ans == QMessageBox.Yes:
            QCloseEvent.accept()  #이벤트 발생을 승인합니다

        else:
            QCloseEvent.ignore() #이벤트 발생을 무시합니



########메뉴바, 상태표시줄 만들기 / 체크메뉴, 컨텍스트 메뉴 만들기############
#체크메뉴는 일반적인 체크표시가 나타나는 것. 컨텍스트 메뉴는 오른클릭을 했을 때 나타나는

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu
#QAction과 같은 경우는 동작(exit)을 추가하기 위해서 추가함
#QMenu는 서브 그룹을 만들기 위한 것
#필요한 창의 요소를 적은 것
#창에다가 메뉴랑 상태표시줄을 만들 수 있음
from PyQt5.QtCore import QCoreApplication

class Exam(QMainWindow): #위에서 언급한 MainWindow 표기하기

    def __init__(self):
        super().__init__()
        self.initUI()
    def __init__(self):
        self.statusBar()  #상태표시줄 만들기 (좌측 하단에 위치한 바)
        self.statusBar().showMessage("안녕하세요")

        menu = self.menuBar() #메뉴생성 #메뉴바 만들기
        menu_file = menu.addMenu('File') #그룹생성 #파일버튼이 만들어 짐 (메뉴의 형태가 만들어짐)
        menu_edit = menu.addMenu('Edit') #그룹생성
        #여기까지는 그냥 형식적인 버튼 모양만 만든 것
        menu_view = menu.addMenu('View')

        file_exit = QAction('Exit', self) #file 안의 exit 표현, 메뉴 객체 생성
        #이제부터 메뉴 객체에 여러 가지를 넣음
        file_exit.setShortcut('Ctrl+Q')
        file_exit.setStatusTip("누르면 영원히 빠이빠이")
        new_txt = QAction("텍스트 파일", self)
        new_py = QAction("파이썬 파일", self)
        #file메뉴 안의 new 메뉴의 작은 서브 메뉴들을 만드는 부분

        view_stat = QAction("상태표시줄", self, checkable=True) #체크박스의 동작칸(checkable)을 지정하는
        view_stat = setChecked(True)
        #이미 체크가 된 상태로 진행

        file_exit.triggered.connect(QCoreApplication.instance().quit)
        #파일이 꺼진 것을 확인하기
        view_stat.triggered.connect(self.tglStat)

        file_new = QMenu('New',self) #QMenu로 서브그룹 만들기(메뉴로 튀어나온 것에서 삼각형으로 확장되는 것)


        menu_file.addMenu(file_new) #서브메뉴 등록
        menu_file.addAction(file_exit)
        #파일 메뉴에 file_exit의 action을 추가한 것 (메뉴등록)
        menu_view.addAction(view_stat) #view그룹에 view_stat이라는 메뉴를 추

        self.resize(450, 400)
        self.show()

    def tglStat(self, state):
        if state:
            self.statusBar().show()
        else :
            self.statusBar().hide()

    def contextMenuEvent(self, QContextMenuEvent):
        cm = QMenu(self)

        quit = cm.addAction("Quit")

        action = cm.exec_(self.mapToGlobal(QContextMenuEvent.pos()))
        if action == quit:
            qApp.quit()


########레이아웃###########

import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QHBoxLayout, QVBoxLayout, QApplication)
#QHBox는 가로, QVBox는 세로

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        #버튼들 생성하기

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        #stretch는 빈 공간을 채워줌
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
#box 레이아웃으로 화면 크기를 조정해도 같은 지정한 위치에 남아 있게 됨
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



######이벤트 & 시그널 공부하기 ######

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QtLCDNumber, QSlider, QVBoxLayout, QApplication)

#공통
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
#여가까지가 공통

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal,self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld) #vbox는 세로로 쌓는 것

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)
        #슬라이드의 값이 변경되었을 때 연결된 슬롯을 정해주는 것. 화면의 숫자가 변화하는 것을 나타내줌

#공통
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slot') #창 이름 지정하기
        self.show()
#여기까지가 공통

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


#####프로젝트에 바로 쓸 이벤트 처리 코드 확인하기######

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn1 = QPushButton("Button1", self)
        btn1.move(30,50)

        btn2 = QPushButton("Button2", self)
        btn2.move(150,50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + 'was pressed')
        #버튼이 눌렸을 때 어떤 버튼이 눌렸는지 표시가 되는 문장을 써줌

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())








