import math
N = int(input())
L =[i for i in range(1, N+1)]
a = sorted(L[:math.floor(N/2)],reverse=True)
b = L[math.floor(N/2):]
result = []

if N%2 == 0:
    for x,y in zip(a,b):
        result.append(y)
        result.append(x)
else:
    for x,y in zip(a,b):
        result.append(y)
        result.append(x)
    result.append(b[-1])
print(*result)


