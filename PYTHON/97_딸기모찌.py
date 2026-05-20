import collections
import sys
input = sys.stdin.readline
q = collections.deque()

Q, V = map(int, input().split())
output_stream = []
storage = 0
for _ in range(Q):
    query = list(map(int,input().split()))

    if query[0] == 1:
        if storage < V:
            temp = min(query[2], V-storage)
            storage += temp
            q.append((query[1], temp))
    elif query[0] == 2:
        num = query[1]
        storage = max(0, storage-num)

        while num > 0 and q:
            x = q.popleft()
            if num < x[1]:
                q.appendleft((x[0], x[1]-num))
                num = 0
            elif num > x[1]:
                num -= x[1]
    else:
        if q:
            output_stream.append(q[0][0])
        else:
            output_stream.append(-1)
        
for i in output_stream:
    print(i)

