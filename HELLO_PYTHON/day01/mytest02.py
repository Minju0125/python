# 홀/짝을 선택하시오 홀
from random import random
mine = input("홀/짝을 선택하시오")

# 나 : 홀
# 컴 : 홀
# 결과 : 이김

com=""
result =""  
rnd = random()

if rnd>0.5:
    com="홀"
else :
    com="짝"

if com==mine:
    result = "이김" 
else : 
    result ="짐" 
print("나:" + mine)  
print("컴:" + com)  
print("결과:" + result)
    