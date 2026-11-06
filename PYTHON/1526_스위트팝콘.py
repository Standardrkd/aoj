N, M = map(int, input().split())
cnt,Sum = 0,0
L = sorted(list(map(int, input().split())), reverse=True)
for i in L:
    Sum += i
    cnt += 1
    if Sum >= M:
        print(cnt)
        break