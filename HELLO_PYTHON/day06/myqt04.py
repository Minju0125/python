import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random
from random import random

form_class = uic.loadUiType("myqt04.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.leMine.returnPressed.connect(self.myclick)
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        mine = self.leMine.text()
        arr=["가위", "바위", "보"]
        rnd = int(random()*3)
        com = arr[rnd]
        result=""
        if mine==com:
            result="비김"
        elif (mine=="가위" and com=="보") or (mine=="보" and com=="바위") or (mine=="바위" and com=="가위"):
            result="이김"
        else :
            result="짐"
        self.leCom.setText(com)
        self.leResult.setText(result);
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = MainClass() 
    myWindow.show()
    app.exec_()