import sys
input=sys.stdin.readline
for i in range(int(input())):
    line=input().split()
    if int(line[0])+int(line[2])==int(line[4]):print("O")
    else:print("X")