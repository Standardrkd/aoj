N = int(input())
a,b = 0,1
mod = 1000000007
for i in range(N):
    a,b = b%mod,(a+b)%mod
print(a)