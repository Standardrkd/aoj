s=sorted(map(int, list(input())),reverse=True)
if s[-1]==0 and sum(s)%3==0:
    for i in s:print(i,end='')
else:print(-1)

