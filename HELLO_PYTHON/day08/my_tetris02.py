import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QPixmap, QLabel
from networkx.generators import line

class Block : 
    def __init__(self):
        self.i = 2
        self.j = 5
        self.type = 7
        self.status = 0
    
    def __str__(self):
        return "{}:{}:{}:{}".format(self.i, self.j, self.type, self.status)

form_class = uic.loadUiType("./my_tetris02.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        #블럭
        self.b2D = [
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],

            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0]
        ]
        
        #스택
        self.s2D = [
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],

            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [4,4,4,4,4,  4,4,0,0,0]
        ]
        
        #화면
        self.d2D = [
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],

            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0]
        ]
        self.l2D = []
        
        self.b = Block()
        
        for i in range(25) :
            line = []
            for j in range(10) : 
                lbl = QLabel(self)
                lbl.setGeometry(31*j, 31*i, 30, 30)
                lbl.setPixmap(QPixmap('0.png'))
                line.append(lbl)
            self.l2D.append(line)

        self.show()
        
        self.setB2D()
        self.setD2D()
        self.myrender()
        self.show2D(self.d2D)
    
    def myrender(self):
        for i in range(25) : 
            for j in range(10) :
                if self.d2D[i][j] == 0 :
                    self.l2D[i][j].setPixmap(QPixmap('0.png'))
                if self.d2D[i][j] == 1 :
                    self.l2D[i][j].setPixmap(QPixmap('1.png'))
                if self.d2D[i][j] == 2 :
                    self.l2D[i][j].setPixmap(QPixmap('2.png'))
                if self.d2D[i][j] == 3 :
                    self.l2D[i][j].setPixmap(QPixmap('3.png'))
                if self.d2D[i][j] == 4 :
                    self.l2D[i][j].setPixmap(QPixmap('4.png'))
                if self.d2D[i][j] == 5 :
                    self.l2D[i][j].setPixmap(QPixmap('5.png'))
                if self.d2D[i][j] == 6 :
                    self.l2D[i][j].setPixmap(QPixmap('6.png'))
                if self.d2D[i][j] == 7 :
                    self.l2D[i][j].setPixmap(QPixmap('7.png'))

    def setB2D(self):
        b = self.b
        if b.type == 7 :
            if b.status ==0 :
                self.b2D[b.i][b.j] = b.type
                self.b2D[b.i][b.j-1] = b.type
                self.b2D[b.i][b.j+1] = b.type
                self.b2D[b.i-1][b.j] = b.type
    
    #b2D + s2D ==> d2D
    def setD2D(self):
        for i in range(25) :
            for j in range(10) : 
                if self.b2D[i][j]>0 :
                    self.d2D[i][j] = self.b2D[i][j]
                if self.s2D[i][j]>0 :
                    self.d2D[i][j] = self.s2D[i][j]
    
    def show2D(self, arr2d):
        for i in range(25) : 
            print(arr2d[i])
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainClass()
    app.exec_()
    