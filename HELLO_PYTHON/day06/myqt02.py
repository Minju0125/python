import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("myqt02.ui")[0] 

class MainClass(QMainWindow, form_class) :
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        a = self.le.text() #가져올때는 text(), 세팅할때는 setText()
        aa = int(a)
        aa *= 2
        self.le.setText(str(aa))
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = MainClass() 
    myWindow.show()
    app.exec_()