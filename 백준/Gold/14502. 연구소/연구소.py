from collections import deque
from itertools import combinations

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

empty = []
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      empty.append((i, j))

q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            q.append((i, j))
def bfs():
  spread = []
  for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            q.append((i, j))
  
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
        graph[nx][ny] = 2
        spread.append((nx, ny))
        q.append((nx, ny))
  return spread

def safe_area():
  return sum(row.count(0) for row in graph)
  
sa = 0
for k in combinations(empty, 3):
  for x, y in k:
    graph[x][y] = 1
  spread = bfs()
  sa = max(sa, safe_area())
  for x, y in spread:
    graph[x][y] = 0
  for x, y in k:
    graph[x][y] = 0

print(sa)
