# 가위바위보 게임
# 가위/바위/보 선택
# 나 : 가위
# 컴 : 가위
# 결과 비김
from random import random
print("가위/바위/보 게임 시작")

mine = input("나 : ")
arr=["가위", "바위", "보"]

rnd = int(random()*3)
com = arr[rnd]

if mine==com:
    print("컴 : " + com)
    print("비김")
elif (mine=="가위" and com=="보") or (mine=="보" and com=="바위") or (mine=="바위" and com=="가위"):
    print("컴 : " + com)
    print("이김")
else :
    print("컴 : " + com)
    print("짐")