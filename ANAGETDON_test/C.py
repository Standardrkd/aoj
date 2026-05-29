import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
L = list(map(int, input().split()))
output = []
d = dict()

for i in L:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for _ in range(Q):
    q = int(input())
    if q in d:
        output.append(str(d[q]))
    else:
        output.append('0')

sys.stdout.write("\n".join(output)+"\n")