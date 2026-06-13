import sys
p=sys.stdin.readline
N=int(p())
L=[]
for i in range(N):L.append(int(p()))
for i in sorted(L):print(i)