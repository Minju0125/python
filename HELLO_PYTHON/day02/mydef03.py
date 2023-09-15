from random import random
def getHollJjak():
    com=""
    rnd = random()
    if rnd>0.5:
        com = "홀"
    else:
        com = "짝"
    return com

com = getHollJjak()
print("com",com)