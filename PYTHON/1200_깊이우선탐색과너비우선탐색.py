import sys
from collections import deque

sys.setrecursionlimit(1000000)
input = sys.stdin.readline
q = deque()

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]


for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N+1):
    graph[i].sort()


def dfs(x):
    print(x, end=" ")
    for v in graph[x]:
        if not visited[v]:
            visited[v] = True
            dfs(v)

def bfs():
    while q:
        x = q.popleft()
        for v in graph[x]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
                print(v, end=" ")


visited = [False] * (N+1)
visited[1] = True
dfs(1)
print()

visited = [False] *(N+1)
visited[1] = True
print(1, end=" ")
q.append(1)
bfs()