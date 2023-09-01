import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("myqt05.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.le.returnPressed.connect(self.myclick)
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        dan = self.le.text()
        danInt = int(dan)
        result=""
        
        # for i in range(1,9+1) :
        #     result +="{} * {} = {}\n".format(danInt, i, i*dan)
        
        result += dan + "*  1 = "  + str(danInt*1) + "\r\n"         
        result += dan + "*  2 = "  + str(danInt*2) + "\r\n"             
        result += dan + "*  3 = "  + str(danInt*3) + "\r\n"             
        result += dan + "*  4 = "  + str(danInt*4) + "\r\n"             
        result += dan + "*  5 = "  + str(danInt*5) + "\r\n"             
        result += dan + "*  6 = "  + str(danInt*6) + "\r\n"             
        result += dan + "*  7 = "  + str(danInt*7) + "\r\n"             
        result += dan + "*  8 = "  + str(danInt*8) + "\r\n"            
        result += dan + "*  8 = "  + str(danInt*9)         
        
        self.te.setText(result);
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = MainClass() 
    myWindow.show()
    app.exec_()