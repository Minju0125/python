import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("myqt08.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        firstStr = self.le_first.text()
        lastStr = self.le_last.text()
        
        first = int(firstStr)
        last = int(lastStr)
        
        result = ""
        for i in range(first, last+1):
            result += "*" * i + "\r\n"
            
        self.te.setText(result)
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = MainClass() 
    myWindow.show()
    app.exec_()