N, K = map(int, input().split())
sizes = []
for i in range(N):
    sizes.append(int(input()))
sizes.sort()
results = []
for i in range(N-1):
    for j in range(N-1,-1,-1):
        if sizes[j] - sizes[i] <= K:
            break
    results.append(j+1-i)
print(max(results))
