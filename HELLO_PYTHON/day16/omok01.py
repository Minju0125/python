import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QPushButton, QSize

form_class = uic.loadUiType("omok01.ui")[0] 

class MainClass(QMainWindow, form_class) :
    def __init__(self) :
        self.flag_wb = True
        
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.arr=[]
        
        for i in range(10):
            for j in range(10):
                lego = QPushButton('', self)
                lego.setIcon(QtGui.QIcon('0.jpg'))
                lego.setIconSize(QSize(40,40))
                lego.setGeometry(i*40, j*40, 40, 40)
                lego.clicked.connect(self.myclick)
                self.arr.append(lego)
            
        self.show()
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        if self.flag_wb:
            btn = self.sender()
            btn.setIcon(QtGui.QIcon('1.jpg'))
            self.flag_wb = not self.flag_wb
        else:
            btn = self.sender()
            btn.setIcon(QtGui.QIcon('2.jpg'))
            self.flag_wb = not self.flag_wb
                
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = MainClass() 
    app.exec_()