from collections import deque

n, m = map(int, input().split())

board = list(range(101))

for _  in range(n):
    x, y = map(int, input().split())
    board[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    board[u] = v

q = deque([(1,0)])
visited = [False] * 101
visited[1] = True

while q:
    pos, dice = q.popleft()

    if pos == 100:
        print(dice)
        break

    for i in range(1, 7):
        res = pos + i

        if res <= 100 and not visited[res]:
            visited[res] = True
            q.append((board[res], dice+1))