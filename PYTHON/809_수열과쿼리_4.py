import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
L = list(map(int, input().split()))
marked = [0 for _ in range(N-1)]

for i in range(N-1):
    if L[i] < L[i+1]:
        marked[i] = 1
    elif L[i] > L[i+1]:
        marked[i] = -1

marked_prefix = [0]
p = 0 
for i in marked:
    p += i 
    marked_prefix.append(p)

for i in range(Q):
    l, r = map(int, input().split())

    if r - l == 1:
        print(marked[l-1])
        continue

    if (r-l) == marked_prefix[r-1] - marked_prefix[l-1]:
        print(1)
    elif (l-r) == marked_prefix[r-1] - marked_prefix[l-1]:
        print(-1)
    else:
        print(0)