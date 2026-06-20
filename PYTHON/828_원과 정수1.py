from math import sqrt
r = int(input())
rsq = r**2
cnt = 0
if sqrt(rsq) == int(sqrt(rsq)):
    cnt = 2
for i in range(-r+1, r):
    if int(sqrt(rsq-pow(i,2))) == sqrt(rsq-pow(i,2)):
        cnt += 2
print(cnt)