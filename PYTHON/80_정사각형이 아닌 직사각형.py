from math import factorial as fac
N = int(input())
m = 0
table = []
for i in range(1, N+1):
    m += pow(i, 2)
result = pow(fac(N+1)//(2*fac(N-1)), 2) - m
print(result)
