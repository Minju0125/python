# 10*25
import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon

form_class = uic.loadUiType("my_tetris01.ui")[0] 

class MainClass(QMainWindow, form_class) :
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        
        self.pb.clicked.connect(self.btnClick)
        self.lbl.mousePressEvent = self.lblClick

        
    def btnClick(self):
        self.lbl.setPixmap(QPixmap('1.png'))
        self.pb.setIcon(QIcon('1.png'))
        
    def lblClick(self, event):
        self.lbl.setPixmap(QPixmap('1.png'))
        self.pb.setIcon(QIcon('1.png'))


        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = MainClass() 
    myWindow.show()
    app.exec_()