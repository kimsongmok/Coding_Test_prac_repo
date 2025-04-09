from collections import deque

m, n = map(int, input().split())
box = []

for _ in range(n):
    t = list(map(int, input().split()))
    box.append(t)

def bfs():
    q = deque()
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                q.append((i, j))
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if box[ny][nx] == 0:
                    box[ny][nx] = box[y][x] + 1
                    q.append((ny, nx))

bfs()

result = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            exit()
        result = max(result, box[i][j])

print(result - 1)