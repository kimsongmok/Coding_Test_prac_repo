n = int(input())
buildings = list(map(int, input().split()))
max_visible = 0

for i in range(n):
    cnt = 0

    for j in range(n):
        if i == j:
            continue

        visible = True
        s, e = min(i, j), max(i, j)

        for k in range(s + 1, e):
            slope = buildings[i] + (buildings[j] - buildings[i]) * (k - i) / (j - i)

            if buildings[k] >= slope:
                visible = False
                break

        if visible:
            cnt += 1

    max_visible = max(max_visible, cnt)

print(max_visible)