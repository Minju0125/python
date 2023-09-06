import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from conda.common._logic import TRUE
from random import random
from PyQt5.Qt import QMessageBox
from PyQt5.uic.properties import QtWidgets


class Block:
    def __init__(self):
        self.i = 2
        self.j = 5
        self.type = int(random()*7)+1
        self.status = 0
    def __str__(self):
        return "{}:{}:{}:{}".format(self.i,self.j,self.type,self.status)

form_class = uic.loadUiType("my_tetris02.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        self.flag_over = False
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
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0]
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
        if self.flag_over :
            return
        
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
            if flag_down :
                self.moveSfromB()
                s = self.s2D[5]
                if(s[0]>0 or
                   s[1]>0 or
                   s[2]>0 or
                   s[3]>0 or
                   s[4]>0 or
                   s[5]>0 or
                   s[6]>0 or
                   s[7]>0 or
                   s[8]>0 
                   ) :
                    QMessageBox.about(self, 'TETRIS', 'GAME OVER')
                    self.flag_over = True
                    
                cnt10 = self.get10Count()
                if cnt10 > 0 :
                    self.remove10(cnt10)
                    cnt_total = int(self.le.text())
                    cnt_total = cnt_total - cnt10
                    self.le.setText(str(cnt_total))
                    if cnt_total<=0:
                        QMessageBox.about(self, 'TETRIS', 'YOU WIN !')
                        self.flag_over = True
                print("cnt10", cnt10)
                self.b.i        = 2
                self.b.j        = 5
                self.b.status   = 0
                self.b.type     = int(random()*7)+1
                self.setB2D()
                
        self.setD2D()
        self.myrender()
        
    def remove10(self, cnt10):
        #임시
        imsi = []
        for s in self.s2D:
            if(s[0]>0 and
               s[1]>0 and
               s[2]>0 and
               s[3]>0 and
               s[4]>0 and
               s[5]>0 and
               s[6]>0 and
               s[7]>0 and
               s[8]>0 and
               s[9]>0 ) :
                pass
            else :
                imsi.append("{},{},{},{},{},{},{},{},{},{}".format(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8],s[9])) #s는 주소지 + 문자열
        
        for i in range(cnt10) : 
            imsi.insert(0, "0,0,0,0,0,0,0,0,0,0")
            
        self.show2D(imsi)
        self.show2D(self.s2D)
                
        for i in range(25):
            ar = imsi[i].split(",")
            self.s2D[i][0]=int(ar[0])
            self.s2D[i][1]=int(ar[1])
            self.s2D[i][2]=int(ar[2])
            self.s2D[i][3]=int(ar[3])
            self.s2D[i][4]=int(ar[4])
            self.s2D[i][5]=int(ar[5])
            self.s2D[i][6]=int(ar[6])
            self.s2D[i][7]=int(ar[7])
            self.s2D[i][8]=int(ar[8])
            self.s2D[i][9]=int(ar[9])
            
    def get10Count(self):
        cnt = 0
        for s in self.s2D:
            if(s[0]>0 and
               s[1]>0 and
               s[2]>0 and
               s[3]>0 and
               s[4]>0 and
               s[5]>0 and
               s[6]>0 and
               s[7]>0 and
               s[8]>0 and
               s[9]>0 ) :
                cnt+=1
        return cnt
        
    def moveSfromB(self):
        for i in range(25):
            for j in range(10):
                if self.b2D[i][j]>0:
                    self.s2D[i][j] = self.b2D[i][j]+10
        
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
                    
                if self.d2D[i][j]== 11:
                    self.l2D[i][j].setPixmap(QtGui.QPixmap("11.png"))    
                if self.d2D[i][j]== 12:
                    self.l2D[i][j].setPixmap(QtGui.QPixmap("12.png"))    
                if self.d2D[i][j]== 13:
                    self.l2D[i][j].setPixmap(QtGui.QPixmap("13.png"))    
                if self.d2D[i][j]== 14:
                    self.l2D[i][j].setPixmap(QtGui.QPixmap("14.png"))    
                if self.d2D[i][j]== 15:
                    self.l2D[i][j].setPixmap(QtGui.QPixmap("15.png"))    
                if self.d2D[i][j]== 16:
                    self.l2D[i][j].setPixmap(QtGui.QPixmap("16.png"))    
                if self.d2D[i][j]== 17:
                    self.l2D[i][j].setPixmap(QtGui.QPixmap("17.png"))    
                if self.d2D[i][j]== 18:
                    self.l2D[i][j].setPixmap(QtGui.QPixmap("18.png"))    
                if self.d2D[i][j]== 19:
                    self.l2D[i][j].setPixmap(QtGui.QPixmap("19.png"))    

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
        for i in range(len(arr2d)):
            print(arr2d[i])
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()