N = int(input())
L = sorted(map(int, input().split()))
for i in range(N):
    if L[i] >= N-i:
        break
print(N-i if sum(L) != 0 else 0)