def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=n or visited[x][y]==1:
        return
    if graph[x][y] == -1:
        visited[x][y] = 1
        return
    visited[x][y] = 1

    dfs(x+graph[x][y],y)
    dfs(x,y+graph[x][y])

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
visited = [[0]*n for _ in range(n)]

dfs(0,0)

if visited[-1][-1] == 1:
    print('HaruHaru')
else:
    print('Hing')


