def f(n):
    r = 1
    for i in range(2,n+1): r *= i
    return r
N,M=map(int, input().split())
print((f(N)//(f(M)*f(N-M)))%1000000007)
