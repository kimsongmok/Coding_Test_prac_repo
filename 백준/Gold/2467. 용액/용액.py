n = int(input())
liq = list(map(int, input().split()))

l, r = 0, n-1
zero = 2000000000
ans_l, ans_r = 0, 0

while l < r:
    mix = liq[l] + liq[r]

    if abs(mix) < abs(zero):
        zero = mix
        ans_l, ans_r = liq[l], liq[r]

    if mix < 0:
        l += 1
    elif mix > 0:
        r -= 1
    else:
        break

print(ans_l, ans_r)