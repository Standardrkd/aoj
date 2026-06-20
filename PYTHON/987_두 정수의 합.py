N, X = map(int, input().split())
L = list(map(int, input().split()))
tp = []
for i in range(N):
    tp.append((L[i], i))
tp.sort()
l,r = 0,N-1
while l<r:
    if tp[l][0] + tp[r][0] < X:
        l += 1
    elif tp[l][0] + tp[r][0] > X:
        r -= 1
    else:
        print(tp[l][1]+1,  tp[r][1]+1)
        exit()
print(-1)