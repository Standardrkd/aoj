import sys
from collections import deque

input = sys.stdin.readline

q = deque()
N, M = map(int, input().split())
maze = []
results = [[200000000 for _ in range(M)] for _ in range(N)] 

for _ in range(N):
    maze.append(list(map(int, input().split())))

dxys = [(-1,0), (1,0), (0,-1), (0,1)]

def in_range(x, y):
    return 0<=x<N and 0<=y<M

def bfs():
    while q:
        x, y, dist = q.popleft()
        for dx, dy in dxys:
            nx = x + dx
            ny = y + dy
            if in_range(nx, ny) and not visited[nx][ny] and maze[nx][ny] == 0:
                q.append((nx, ny, dist + 1))
                results[nx][ny] = min(results[nx][ny], dist+1)
                visited[nx][ny] = True

visited = [[False for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if (i == 0 or i == N-1 or j == 0 or j == M-1) and maze[i][j] != 1:
            q.append((i, j, 0))
            results[i][j] = 0
            visited[i][j] = True
bfs() 

Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())
    if results[a-1][b-1] == 200000000:
        print(-1)
    else:
        print(results[a-1][b-1])