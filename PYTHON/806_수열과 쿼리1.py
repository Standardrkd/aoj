import sys
input = sys.stdin.readline
N, M = map(int, input().split())
L = list(map(int, input().split()))

prefix = 0
prefix_list = [0]
for i in L:
    prefix += i
    prefix_list.append(prefix)

for _ in range(M):
    a, b = map(int, input().split())
    print(prefix_list[b] - prefix_list[a-1])