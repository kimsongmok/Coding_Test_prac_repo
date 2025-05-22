n, c = map(int, input().split())
router = [int(input()) for _ in range(n)]
router.sort()

left = 1
right = router[-1] - router[0]
res = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 1
    last = router[0]

    for i in range(1, n):
        if router[i] - last >= mid:
            cnt += 1
            last = router[i]

    if cnt >= c:
        res = mid
        left = mid + 1

    else:
        right = mid - 1

print(res)