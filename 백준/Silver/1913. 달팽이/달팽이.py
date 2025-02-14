N = int(input())
target = int(input())

grid = [[0] * N for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = N // 2, N // 2
num = 1
grid[x][y] = num

target_x, target_y = x + 1, y + 1

step = 1
direction = 0

while num < N * N:
    for _ in range(2):
        for _ in range(step):
            if num >= N * N:
                break
            x += dx[direction]
            y += dy[direction]
            num += 1
            grid[x][y] = num

            if num == target:
                target_x, target_y = x + 1, y + 1

        direction = (direction + 1) % 4

    step += 1

for row in grid:
    print(*row)
print(target_x, target_y)