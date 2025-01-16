n = int(input())

t = [0 for _ in range(n+1)]
p = [0 for _ in range(n+1)]
for i in range(1, n+1):
  t[i], p[i] = map(int, input().split())

dp = [0 for _ in range(n+1)]
for j in range(1, n+1):
  dp[j] = max(dp[j], dp[j-1])
  date = j + t[j] - 1
  if date <= n:
    dp[date] = max(dp[date], dp[j-1]+p[j])

print(max(dp))