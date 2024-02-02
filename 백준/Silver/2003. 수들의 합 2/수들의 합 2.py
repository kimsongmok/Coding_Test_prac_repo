n, m = map(int, input().split())
li = list(map(int, input().split()))
cnt = 0
sum_lr = 0
right = 0

for left in range(n):
    while sum_lr < m and right < n:
        sum_lr += li[right]
        right += 1
    if sum_lr == m:
        cnt += 1
    sum_lr -= li[left]

print(cnt)