import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
prime = [True] * (N+1)
prime[0], prime[1] = False, False
prefix = 0
prefix_list = []
for i in range(2,N+1):
    if prime[i]:
        for j in range(2*i, N+1, i):
            prime[j] = False
for i in prime:
    if i:
        prefix += 1
    prefix_list.append(prefix)
for _ in range(Q):
    i, j = map(int, input().split())
    print(prefix_list[j]-prefix_list[i-1])