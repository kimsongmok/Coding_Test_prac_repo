n, m = map(int, input().split())
tree = list(map(int, input().split()))

l, r =  0, max(tree)
ans = 0

while l <= r:
    mid = (l+r)//2
    wood = 0

    for i in tree:
        if i >= mid:
            wood += i - mid

    if wood >= m:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)