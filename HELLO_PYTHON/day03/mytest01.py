# up&down 게임
# 1~99까지의 숫자
# 숫자를 맞춰보세요

from random import random
com = int(random()*99+1)

while True:
        myNum = input("숫자를 입력하세요. ==>")
        imine = int(myNum)
    
        if com>imine :
            print("{}\tUP".format(myNum))
        elif com<imine :
            print("{}\tDOWN".format(myNum))
        else : 
            print("정답입니다.")
            break



    
