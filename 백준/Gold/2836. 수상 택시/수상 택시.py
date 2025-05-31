n, m = map(int, input().split())

back = []

for _ in range(n):
    s, e = map(int, input().split())
    if s > e:
        back.append((e, s))

back.sort()

cnt = 0
i = 0

while i < len(back):

    des_min = back[i][0]
    des_max = back[i][1]
    i += 1

    while i < len(back) and back[i][0] <= des_max:
        des_min = min(des_min, back[i][0])
        des_max = max(des_max, back[i][1])
        i += 1

    cnt += 2* (des_max - des_min)

print(cnt + m)