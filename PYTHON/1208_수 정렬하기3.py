import sys
input=sys.stdin.readline
N=int(input())
L=[0 for _ in range(100002)]
for i in range(N):L[int(input())]+=1
for i in range(100002):
    for _ in range(L[i]):print(i)