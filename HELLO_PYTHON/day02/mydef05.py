def add_min_mul_div(a,b):
    #멀티리턴 받을 때 배열로 받음 tuple
    return a+b, a-b, a*b, a/b #튜플로 나옴 (작은 배열) -> 배열처럼 씀
sum = add_min_mul_div(4,2)

print("sum",sum)
