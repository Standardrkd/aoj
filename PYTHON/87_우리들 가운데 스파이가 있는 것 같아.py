T = int(input())
for _ in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    t = tuple(set(L))
    a,b = t
    print(L.index(b)+1 if L.count(a) > L.count(b) else L.index(a)+1)
    # 정답을 맞혔어요 
    # 엥..?