n, k = map(int, input().split())
coins=[]
ans = 0
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

for coin in coins:
    if k >= coin:
        ans += k//coin
        k %= coin
        if k<=0:
            break

print(ans)