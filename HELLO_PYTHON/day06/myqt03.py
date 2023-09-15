import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("myqt03.ui")[0] 

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        arr=[1,2,3,4,5, 6,7,8,9,10,
             1,12,13,14,15, 16,17,18,19,20,
             21,22,23,24,25, 26,27,28,29,30,
             31,32,33,34,35, 36,37,38,39,40,
             41,42,43,44,45]

        arr6=[]
        
        for i in range(1000):
            rnd= int(random()*45)
            a=arr[0]
            arr[0]=arr[rnd]
            arr[rnd]=a
            
        arr6.append(arr[0])
        arr6.append(arr[1])
        arr6.append(arr[2])
        arr6.append(arr[3])
        arr6.append(arr[4])
        arr6.append(arr[5])
        
        for i in range(6):
            for j in range (6):
                if arr6[i]<arr6[j]:
                    a = arr6[i]
                    b = arr6[j]
                    arr6[i]= b
                    arr6[j] =a
        print(arr6)
        
        self.le1.setText(str(arr6[0]))
        self.le2.setText(str(arr6[1]))
        self.le3.setText(str(arr6[2]))
        self.le4.setText(str(arr6[3]))
        self.le5.setText(str(arr6[4]))
        self.le6.setText(str(arr6[5]))
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = MainClass() 
    myWindow.show()
    app.exec_()