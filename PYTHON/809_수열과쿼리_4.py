N, Q = map(int, input().split())
L = list(map(int, input().split()))
marked = [0 for _ in range(N)]

# 상승, 감소 부분 마킹해놓는다. range가 1, 2 일땐 예외처리 그 외의 경우는 규칙 따라
for i in range(N-1):
    if L[i] < L[i+1]:
        marked[i], marked[i+1] = (1,1)
       
for i in range(Q):
    l, r = map(int, input().split())