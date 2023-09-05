import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from conda.common._logic import TRUE
from sqlalchemy.sql.expression import false
from random import random

class Block:
    def __init__(self):
        self.i = 2
        self.j = 5
        self.type = 1
        self.status = 0
    def __str__(self):
        return "{}:{}:{}:{}".format(self.i,self.j,self.type,self.status)

form_class = uic.loadUiType("my_tetris02.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.b2D=[
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            
            
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0]
        ]
        self.s2D=[
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            
            
            [0,0,0,0,0, 0,0,0,0,0],
            [4,4,4,4,4, 4,4,4,0,0],
            [4,4,4,4,4, 4,4,4,0,0],
            [4,4,4,4,4, 4,4,4,4,0],
            [4,4,4,4,4, 4,4,4,4,0]
        ]
        
        self.d2D=[
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            
            
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0]
        ]
        self.l2D = []
        
        self.b = Block()
        
        for i in range(25):
            line = []
            for j in range(10):
                lbl = QLabel(self)
                lbl.setPixmap(QtGui.QPixmap("0.png"))
                lbl.setGeometry(j*31,i*31, 40, 40)
                line.append(lbl)
            self.l2D.append(line)
        
        self.show()
        
        self.setB2D()
        self.setD2D()
        self.myrender()
        self.show2D(self.d2D)
        
    def keyPressEvent(self, e):
        bak_i = self.b.i
        bak_j = self.b.j
        bak_s = self.b.status
        
        flag_down = False
        
        k = e.key()
        if k == 65: #A
            self.b.j -= 1
        if k == 68: #D
            self.b.j += 1
        if k == 87: #W
            self.changeStatus()
        if k == 83: #S
            self.b.i += 1
            flag_down = True
        
        flag_rb = False
        try:
            self.setB2D()
        except:
            flag_rb = True
            
        flag_l = self.isCrash()
        flag_s = self.isCrashStack()
        
        if flag_rb or flag_l or flag_s:
            self.b.i        = bak_i
            self.b.j        = bak_j
            self.b.status   = bak_s
            self.setB2D()
            if flag_down:
               self.moveSfromB()
               self.b.i = 2
               self.b.j = 5
               self.b.status = 0
               self.b.type = int(random()*7) +1
               self.setB2D()
               self.removeRows()
        
        self.setD2D()
        self.myrender()
        
    
    def removeRows(self):
        for i in range(25):
            if (self.d2D[i][0]> 0 and 
               self.d2D[i][1]> 0 and 
               self.d2D[i][2]> 0 and 
               self.d2D[i][3]> 0 and 
               self.d2D[i][4]> 0 and 
               self.d2D[i][5]> 0 and 
               self.d2D[i][6]> 0 and 
               self.d2D[i][7]> 0 and 
               self.d2D[i][8]> 0 and 
               self.d2D[i][9]> 0 ) :
    
    
    def moveSfromB(self):
        for i in range(25):
            for j in range(10):
                if self.b2D[i][j]>0 :
                    self.s2D[i][j] = self.b2D[i][j]
        
    def isCrashStack(self):
        for i in range(25):
            for j in range(10):
                if self.b2D[i][j]>0 and self.s2D[i][j]>0:
                    return True
        return False

        
    def isCrash(self):
        if self.b.j < 0:
            return True
        
        cnt = 0
        for i in range(25):
            if self.b2D[i][0]>0 and self.b2D[i][9]>0:
                return True
            for j in range(10):
                    cnt +=1
        if cnt <4:
            return True
        else:
            return False

    def changeStatus(self):
        b = self.b
        if b.type == 2 or b.type == 3 or b.type == 4:
            if b.status == 0:
                b.status = 1
            elif b.status == 1:
                b.status = 0
        if b.type == 5 or b.type == 6 or b.type == 7:
            if b.status == 0:
                b.status = 1
            elif b.status == 1:
                b.status = 2
            elif b.status == 2:
                b.status = 3  
            elif b.status == 3:
                b.status = 0
                
        
    def myrender(self):
        for i in range(25):
            for j in range(10):
                if self.d2D[i][j]== 0:
                    self.l2D[i][j].setPixmap(QtGui.QPixmap("0.png"))
                if self.d2D[i][j]== 1:
                    self.l2D[i][j].setPixmap(QtGui.QPixmap("1.png"))
                if self.d2D[i][j]== 2:
                    self.l2D[i][j].setPixmap(QtGui.QPixmap("2.png")) 
                if self.d2D[i][j]== 3:
                    self.l2D[i][j].setPixmap(QtGui.QPixmap("3.png"))
                if self.d2D[i][j]== 4:
                    self.l2D[i][j].setPixmap(QtGui.QPixmap("4.png"))
                if self.d2D[i][j]== 5:
                    self.l2D[i][j].setPixmap(QtGui.QPixmap("5.png"))
                if self.d2D[i][j]== 6:
                    self.l2D[i][j].setPixmap(QtGui.QPixmap("6.png")) 
                if self.d2D[i][j]== 7:
                    self.l2D[i][j].setPixmap(QtGui.QPixmap("7.png"))
                    

    def setB2D(self):
        for i in range(25):
            for j in range(10):
                self.b2D[i][j] = 0
                
        b = self.b
        if b.type == 1 :
            self.b2D[b.i    ][b.j   ] = b.type 
            self.b2D[b.i    ][b.j+1 ] = b.type 
            self.b2D[b.i+1  ][b.j   ] = b.type
            self.b2D[b.i+1  ][b.j+1 ] = b.type 
            
        if b.type == 2 :
            if b.status == 0:
                self.b2D[b.i    ][b.j   ] = b.type 
                self.b2D[b.i-1  ][b.j   ] = b.type 
                self.b2D[b.i    ][b.j+1 ] = b.type 
                self.b2D[b.i+1  ][b.j+1 ] = b.type 
            if b.status == 1:
                self.b2D[b.i    ][b.j   ] = b.type 
                self.b2D[b.i    ][b.j+1 ] = b.type 
                self.b2D[b.i+1  ][b.j-1 ] = b.type 
                self.b2D[b.i+1  ][b.j   ] = b.type 

        if b.type == 3 :
            if b.status == 0:
                self.b2D[b.i    ][b.j   ] = b.type 
                self.b2D[b.i-1  ][b.j   ] = b.type 
                self.b2D[b.i    ][b.j-1 ] = b.type 
                self.b2D[b.i+1  ][b.j-1 ] = b.type
            if b.status == 1:
                self.b2D[b.i    ][b.j   ] = b.type 
                self.b2D[b.i-1  ][b.j-1 ] = b.type 
                self.b2D[b.i-1  ][b.j   ] = b.type 
                self.b2D[b.i    ][b.j+1 ] = b.type 

        if b.type == 4 :
            if b.status == 0:
                self.b2D[b.i    ][b.j   ] = b.type 
                self.b2D[b.i-1  ][b.j   ] = b.type 
                self.b2D[b.i+1  ][b.j   ] = b.type 
                self.b2D[b.i+2  ][b.j   ] = b.type 
            if b.status == 1:
                self.b2D[b.i    ][b.j   ] = b.type 
                self.b2D[b.i    ][b.j-1 ] = b.type 
                self.b2D[b.i    ][b.j+1 ] = b.type 
                self.b2D[b.i    ][b.j+2 ] = b.type 
                
        if b.type == 5 :
            if b.status == 0:
                self.b2D[b.i    ][b.j   ] = b.type 
                self.b2D[b.i-1  ][b.j-1 ] = b.type 
                self.b2D[b.i    ][b.j-1 ] = b.type 
                self.b2D[b.i    ][b.j+1 ] = b.type 
            if b.status == 1:
                self.b2D[b.i    ][b.j   ] = b.type 
                self.b2D[b.i-1  ][b.j   ] = b.type 
                self.b2D[b.i-1  ][b.j+1 ] = b.type 
                self.b2D[b.i+1  ][b.j   ] = b.type 
            if b.status == 2:
                self.b2D[b.i    ][b.j   ] = b.type 
                self.b2D[b.i    ][b.j-1 ] = b.type 
                self.b2D[b.i    ][b.j+1 ] = b.type 
                self.b2D[b.i+1  ][b.j+1 ] = b.type 
            if b.status == 3:
                self.b2D[b.i    ][b.j   ] = b.type 
                self.b2D[b.i-1  ][b.j   ] = b.type 
                self.b2D[b.i+1  ][b.j   ] = b.type 
                self.b2D[b.i+1  ][b.j-1 ] = b.type 
                
        if b.type == 6 :
            if b.status == 0:
                self.b2D[b.i    ][b.j   ] = b.type 
                self.b2D[b.i    ][b.j-1 ] = b.type 
                self.b2D[b.i    ][b.j+1 ] = b.type 
                self.b2D[b.i-1  ][b.j+1 ] = b.type 
            if b.status == 1:
                self.b2D[b.i    ][b.j   ] = b.type 
                self.b2D[b.i-1  ][b.j   ] = b.type 
                self.b2D[b.i+1  ][b.j   ] = b.type 
                self.b2D[b.i+1  ][b.j+1 ] = b.type    
            if b.status == 2:
                self.b2D[b.i    ][b.j   ] = b.type 
                self.b2D[b.i    ][b.j-1 ] = b.type 
                self.b2D[b.i    ][b.j+1 ] = b.type 
                self.b2D[b.i+1  ][b.j-1 ] = b.type 
                
            if b.status == 3:
                self.b2D[b.i    ][b.j   ] = b.type 
                self.b2D[b.i-1  ][b.j-1 ] = b.type 
                self.b2D[b.i-1  ][b.j   ] = b.type 
                self.b2D[b.i+1  ][b.j   ] = b.type 

            
        if b.type == 7 :
            if b.status == 0:
                self.b2D[b.i    ][b.j   ] = b.type 
                self.b2D[b.i    ][b.j-1 ] = b.type 
                self.b2D[b.i-1  ][b.j   ] = b.type 
                self.b2D[b.i    ][b.j+1 ] = b.type 
            if b.status == 1:
                self.b2D[b.i    ][b.j   ] = b.type 
                self.b2D[b.i-1  ][b.j   ] = b.type 
                self.b2D[b.i+1  ][b.j   ] = b.type 
                self.b2D[b.i    ][b.j+1 ] = b.type 
            if b.status == 2:
                self.b2D[b.i    ][b.j   ] = b.type 
                self.b2D[b.i    ][b.j-1 ] = b.type 
                self.b2D[b.i    ][b.j+1 ] = b.type 
                self.b2D[b.i+1  ][b.j   ] = b.type 
            if b.status == 3:
                self.b2D[b.i    ][b.j   ] = b.type 
                self.b2D[b.i    ][b.j-1 ] = b.type 
                self.b2D[b.i-1  ][b.j   ] = b.type 
                self.b2D[b.i+1  ][b.j   ] = b.type 
                
                
                
    def setD2D(self):
        for i in range(25):
            for j in range(10):
                self.d2D[i][j] = 0
        for i in range(25):
            for j in range(10):
                if self.b2D[i][j]>0:
                    self.d2D[i][j]=self.b2D[i][j] 
                if self.s2D[i][j]>0:
                    self.d2D[i][j]=self.s2D[i][j] 
                    

    def show2D(self,arr2d):
        for i in range(25):
            print(arr2d[i])
        
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()