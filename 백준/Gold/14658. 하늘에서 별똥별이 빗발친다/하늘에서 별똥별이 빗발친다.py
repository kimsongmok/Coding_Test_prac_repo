n, m, l, k = map(int, input().split())
stars = []
max_cnt = 0

for _ in range(k):
    x, y = map(int, input().split())
    stars.append((x,y))

for i in range(k):
    for j in range(k):
        corner_x = stars[i][0]
        corner_y = stars[j][1]
        cnt = 0

        for x, y in stars:
            if corner_x <= x <= corner_x + l and corner_y <= y <= corner_y + l:
                cnt += 1

        max_cnt = max(max_cnt, cnt)

print(k-max_cnt)