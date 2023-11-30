n = int(input())
box = [0]*1001
dp = [1 for _ in range(n)]

box = list(map(int, input().split()))

for i in range(1, n):
    for j in range(i):
        if box[i] > box[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))