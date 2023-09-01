import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random
from PyQt5.Qt import QMessageBox

form_class = uic.loadUiType("myqt07.ui")[0]
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.myclick)
        self.com =ranCom(self)
   
    def ranCom():
        arr = [1,2,3,4,5,6,7,8,9]
        for i in range (100):
            rnd = int(random()*9)
            a = arr[0]
            arr[0]=arr[rnd]
            arr[rnd]=a
        return "{}{}{}".format(arr[0], arr[1], arr[2])
   
    def getS(self, mine, com):
        cnt=0;
        #substring
        m1 =mine[0:1] 
        m2 =mine[1:2] 
        m3 =mine[2:3]
        
        c1 =com[0:1]
        c2 =com[1:2] 
        c3 =com[2:3]
        
        if m1==c1 : cnt+=1
        if m2==c2 : cnt+=1
        if m3==c3 : cnt+=1
        
        return cnt
   
    def getB(self, mine, com):
        cnt=0;
        #substring
        m1 =mine[0:1] 
        m2 =mine[1:2] 
        m3 =mine[2:3]
        
        c1 =com[0:1]
        c2 =com[1:2] 
        c3 =com[2:3]
        
        if m1==c2 or m1==c3 : cnt+=1
        if m2==c1 or m2==c3 : cnt+=1
        if m3==c1 or m3==c2 : cnt+=1
        
        return cnt
       
    def myclick(self):
        mine = self.le.text()
        s = self.getS(mine, self.com)
        b = self.getB(mine, self.com)
        str_new = "{}\t{}S{}B\t".format(mine,s,b)
        str_old= self.pte.toPlainText()
        self.pte.appendPlainText(str_new)
        self.le.setText("")
        if s==3 :
            QMessageBox.about(self, '야구게임', mine + ' 이겼습니다.')
        print(str_new, str_old)
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = MainClass() 
    myWindow.show()
    app.exec_()