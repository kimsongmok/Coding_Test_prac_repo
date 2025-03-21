from collections import deque

n = int(input())
k = int(input())

apple = set()
rotate = deque()
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(k):
    x, y = map(int, input().split())
    apple.add((x-1,y-1))

l = int(input())

for _ in range(l):
    x, c = input().split()
    rotate.append((int(x), c))

board = [[0]*n for _ in range(n)]
snake = deque([(0,0)])
board[0][0] = 1

time = 0
direction = 0

while True:
    time += 1
    head_x, head_y = snake[0]

    nx = head_x + dx[direction]
    ny = head_y + dy[direction]

    if nx < 0 or nx >= n or ny < 0 or ny >= n or (nx, ny) in snake:
        break

    if (nx, ny) in apple:
        apple.remove((nx, ny))
        snake.appendleft((nx, ny))
    else:
        snake.appendleft((nx, ny))
        snake.pop()

    if rotate and time == rotate[0][0]:
        x, c = rotate.popleft()
        if c == 'D':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4

print(time)