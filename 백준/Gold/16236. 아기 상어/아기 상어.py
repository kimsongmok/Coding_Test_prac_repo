from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            ax, ay = i, j
            graph[i][j] = 0

size = 2
eat = 0
time = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, size):
    visited = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    fishes = []

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if graph[nx][ny] <= size:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

                    if 0 < graph[nx][ny] < size:
                        fishes.append((visited[nx][ny], nx, ny))

    fishes.sort()
    return fishes


while True:
    fish_list = bfs(ax, ay, size)
    if not fish_list:
        break

    dist, nx, ny = fish_list[0]
    time += dist
    ax, ay = nx, ny
    graph[nx][ny] = 0
    eat += 1

    if eat == size:
        size += 1
        eat = 0

print(time)