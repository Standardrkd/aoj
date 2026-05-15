N, T = map(int,input().split())
factors = set()
cnt = 0
for i in range(1,T+1):
    if T%i == 0:
        factors.add(i)
factors = sorted(list(factors))
bulb = list(map(int, input().split()))

for i in bulb:
    m = 1001    
    if i in factors:
        continue
    else:
        for j in factors:
            tmp = abs(i-j)
            if tmp < m:
                m = tmp
        cnt += m
print(cnt)