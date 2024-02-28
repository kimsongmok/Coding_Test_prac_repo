from collections import deque

n = int(input())
graph = []
visited = [[0] * (n) for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

def bfs(idx):
    q = deque()
    q.append(idx)
    temp = [0 for _ in range(n)]
    
    while q:
        x = q.popleft()
        
        for i in range(n):
            if temp[i] == 0 and graph[x][i] == 1:
                q.append(i)
                temp[i] = 1
                visited[idx][i] = 1

for i in range(n):
    bfs(i)

for i in visited:
    print(*i)