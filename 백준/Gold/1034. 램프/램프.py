n, m = map(int, input().split())
switch = []
res = 0
for _ in range(n):
    lamp = input()
    switch.append(lamp)
k = int(input())
uni_switch = set(switch)
for i in uni_switch:
    zero_cnt = i.count('0')
    cnt = switch.count(i)

    if zero_cnt <= k and zero_cnt % 2 == k % 2:
        res = max(res, cnt)

print(res)