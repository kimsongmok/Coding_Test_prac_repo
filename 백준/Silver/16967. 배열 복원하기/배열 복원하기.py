h, w, x, y = map(int, input().split())
a = [[0]*w for _ in range(h)]
b = []
for _ in range(h + x):
    b.append(list(map(int, input().split())))

for i in range(h):
    for j in range(w):
        a[i][j] = b[i][j]

for k in range(x, h):
    for l in range(y, w):
        a[k][l] -= a[k-x][l-y]

for m in range(len(a)):
    print(*a[m])