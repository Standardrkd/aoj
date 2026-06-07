N = int(input())
L = list(map(int, input().split()))
results = []
prefix = 0
for i in range(N-1):
    x = L[i+1] - L[i]
    if x > 0:
        prefix += x
        results.append(prefix)
    else:
        prefix = 0
print(results)
print(max(results) if results else 0)
    
