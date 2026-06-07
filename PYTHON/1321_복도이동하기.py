import sys
input = sys.stdin.readline
N, M = map(int, input().split())
cnt = 0
d = 1
L = []
for _ in range(M):
    a, b = map(int, input().split())
    L.append((a,b))
L = sorted(L, key=lambda x:x[1])
for a,b in L:
    if a == 1 and d == 1:
        cnt += 1
        d = 2
    elif a == 2 and d == 2:
        cnt += 1
        d = 1

if d == 1:
    print(N+cnt)
else:
    print(N-1+cnt)