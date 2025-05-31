n = int(input())

start = list(map(int, input()))
target = list(map(int, input()))

light_max = 1000000
res = light_max

arr = start[:]
cnt = 0

for i in range(1, n):
    if arr[i - 1] != target[i - 1]:
        for j in range(i - 1, i + 2):
            if 0 <= j < n:
                arr[j] = 1 - arr[j]
        cnt += 1

if arr == target:
    res = cnt


arr = start[:]
cnt = 1

for k in range(0, 2):
    arr[k] = 1 - arr[k]

for l in range(1, n):
    if arr[l - 1] != target[l - 1]:
        for m in range(l - 1, l + 2):
            if 0 <= m < n:
                arr[m] = 1 - arr[m]
        cnt += 1

if arr == target:
    res = min(res, cnt)

if res == light_max:
    print(-1)
else:
    print(res)