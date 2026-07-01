import sys
input = sys.stdin.readline
N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
first = 0
if N == 2:
    print(1,1)
else:
    first = (mat[0][1] + mat[0][2] - mat[1][2])//2
    for i in range(N):
        print(abs(mat[0][i] - first), end=' ')