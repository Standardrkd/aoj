N = int(input())
s = list(map(int, input().split()))
if N <= 3:
    print(s[N-1])
    exit()
dp = [0] * (N)
dp[1], dp[2], dp[3] = s[1], s[2], s[1]+s[3]
for i in range(4, N):
    dp[i] = max(s[i] + dp[i-2], s[i] + dp[i-3])
print(dp[-1])