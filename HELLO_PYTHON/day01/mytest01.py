# arr=range(1, 11)
# sum=0
# for i in arr :
#     sum=sum+i
# print(sum)
from aioitertools.builtins import sum

sum = 0
for i in range(1, 10+1):
    sum += i
print(sum)