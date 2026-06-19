import sys
input = sys.stdin.readline
N, M = map(int, input().split())
L = list(map(int, input().split()))

evenList = [0]
oddList = [0]
odd_prefix = 0
even_prefix = 0

for i in range(N):
    odd_prefix = odd_prefix + L[i] if i%2 == 0 else odd_prefix - L[i]
    even_prefix = even_prefix + L[i] if i%2 == 1 else even_prefix - L[i]
    oddList.append(odd_prefix)
    evenList.append(even_prefix)


for i in range(M):
    a, b = map(int, input().split())
    print(evenList[b] - evenList[a-1] if a%2 == 0 else oddList[b] - oddList[a-1])
