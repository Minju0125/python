from random import random
def ranCom() :
    arr = [1,2,3,4,5,6,7,8,9]
    for i in range (100):
        rnd = int(random()*9)
        a = arr[0]
        arr[0]=arr[rnd]
        arr[rnd]=a
    return "{}{}{}".format(arr[0], arr[1], arr[2])

def getS(mine, com):
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

def getB(mine, com):
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

com = ranCom()
print("com", com)
while True :
    mine = input("세숫자를 입력하세요")
    s=getS(mine, com)
    b=getB(mine, com)
    if s==3 :
        print("{}\t{}S{}B\t".format(mine,s,b))
        break
    else :
        print("{}\t{}S{}B".format(mine,s,b))
