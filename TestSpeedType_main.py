from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

from TestSpeedType import Ui_PagesWindow
from Loading_type import Ui_MainWindow

class LoadingMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton.clicked.connect(self.click)
        self.show()

    def mousePressEvent(self , evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self , evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()
    
    def click(self):
        self.panel=RootMain()
        self.panel.show()
        self.close()

        

class RootMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_PagesWindow()
        self.ui.setupUi(self)

        self.ui.btn_test.clicked.connect(lambda: [self.ui.pages.setCurrentWidget(self.ui.page_test) , self.ui.btn_test.setStyleSheet('background: rgb(25, 106, 72);color: #fff;  border-radius: 4px;'),
        self.ui.btn_setting.setStyleSheet('background:rgb(211, 221, 221); border-radius: 4px;')
        
        ])

        self.ui.btn_setting.clicked.connect(lambda: [self.ui.pages.setCurrentWidget(self.ui.page_setting) , self.ui.btn_setting.setStyleSheet('background: rgb(25, 106, 72);color: #fff;  border-radius: 4px;'),
        self.ui.btn_test.setStyleSheet('background:rgb(211, 221, 221); border-radius: 4px;')
        ])

        
        # removing borders
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        

    def main(self):
        self.mainwindow = RootMain()
        self.mainwindow.show()
        self.close()

    def mousePressEvent(self , evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self , evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = LoadingMain()
    sys.exit(app.exec_())