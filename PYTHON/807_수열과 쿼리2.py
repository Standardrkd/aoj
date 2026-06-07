N, M = map(int, input().split())
L = list(map(int, input().split()))

prefix = 1
prefix_list = [1]
for i in L:
    if i > 0:
        prefix *= 1
    else:
        prefix *= -1
    prefix_list.append(prefix)

for _ in range(M):
    a, b = map(int, input().split())
    print(1 if prefix_list[b] // prefix_list[a-1] > 0 else -1)
