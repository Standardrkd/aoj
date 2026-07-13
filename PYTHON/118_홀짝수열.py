N=int(input())
cnt_o,cnt_e=0,0
L=list(map(int,input().split()))
for i in L:
    if i&1:
        cnt_o+=1
    else:
        cnt_e+=1
if N&1:
    if cnt_e+1==cnt_o:
        print(1)
    else:
        print(0)
else:
    if cnt_e==cnt_o:
        print(1)
    else:
        print(0)