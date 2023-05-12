from collections import deque
from itertools import combinations
from copy import deepcopy


n, m = map(int, input().split())
graph = []
temp1 = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            temp1.append((i, j))

li = list(combinations(temp1,3))

ans = 0
for i in li:
    graph2 = deepcopy(graph)
    for x,y in i:
        graph2[x][y] = 1
    q = deque()
    for k in range(n):
        for l in range(m):
            if graph2[k][l] == 2:
                q.append((k, l))
    while q:
        x, y = q.popleft()
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx <n and 0<= ny <m:
                if graph2[nx][ny]:
                    continue
                graph2[nx][ny] = 1 #1이던 어떤 숫자던 상관이 없다.
                q.append((nx, ny))
    cnt = 0
    for k in range(n):
        for l in range(m):
            if graph2[k][l] == 0:
                cnt +=1
    ans = max(ans, cnt)

print(ans)