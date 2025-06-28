n, k = map(int, input().split())
coins = []

for _ in range(n):
    coin = int(input())
    coins.append(coin)

dp = [0] * (k + 1)
dp[0] = 1
for i in coins:
    for j in range(i, k + 1):
        dp[j] += dp[j - i]
print(dp[k])