import math
n, l = map(int, input().split())
pool = []
pos = 0
res = 0
for _ in range(n):
    s, e = map(int, input().split())
    pool.append([s,e])

new_pool = sorted(pool)

for s, e in new_pool:
    if pos < s:
        pos = s

    board = math.ceil((e-pos)/l)
    res += board
    pos += board*l

print(res)