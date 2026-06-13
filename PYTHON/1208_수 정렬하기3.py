import sys
p=sys.stdin.readline
N=int(p())
d = dict()
for _ in range(N): 
    x = int(p())
    if x in d:
        d[x]+=1
    else:
        d[x] = 1
for k,v in sorted(d.items()):
    for _ in range(v):
        print(k)