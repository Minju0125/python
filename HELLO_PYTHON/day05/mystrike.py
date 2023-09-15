# 세 숫자를 입력하시오 - 3,2,5
from random import random

arrRnd = list(range(1,9+1))
for i in range(10000):
    rnd = int(random()*9)
    a = arrRnd[0]
    arrRnd[0]=arrRnd[rnd]
    arrRnd[rnd]=a
arrCom=[]
arrCom.append(arrRnd[0])
arrCom.append(arrRnd[1])
arrCom.append(arrRnd[2])

print("세 숫자를 입력하시오. (0~9)\n")

arrMine=[]
for i in range(1, 3+1):
    num = input(str(i) +" 번째 수 입력 ==>")
    numInt = int(num)
    arrMine.append(numInt)
print("내가 입력한 수 =>" + str(arrMine))
print("컴퓨터 수 => " + str(arrCom))

strike=0
ball=0
out=0
# for문을 돌면서 i 인덱스도 같고 값도 같으면 스트라이크 ++
# 값만 같으면 볼
for i in range(2+1):
    for j in range(2+1):
        if(i==j and arrCom[i]==arrMine[j]):
            strike = strike+1
        elif(arrCom[i]==arrMine[j]):
            ball = ball+1
print("{}S {}B".format(strike, ball, out))
