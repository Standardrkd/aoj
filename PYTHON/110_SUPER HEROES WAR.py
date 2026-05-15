from collections import deque
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())

    enemies = deque(sorted(list(map(int, input().split()))))

    for i in range(N):
        enemy = enemies[0]

        if enemy < K:
            K += enemies.popleft()
        elif enemy == K:
            enemies.popleft()
            break
        else:
            break
    if enemies:
        print("NO")
    else:
        print("YES")
    
    