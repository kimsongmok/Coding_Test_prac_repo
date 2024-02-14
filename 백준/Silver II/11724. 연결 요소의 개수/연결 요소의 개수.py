import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**3)

def dfs(idx):
    global visited, graph
    visited[idx] = True
    
    for i in range(1, n+1):
        if not visited[i] and graph[idx][i]:
            dfs(i)
    

MAX = 1000+10
n,m = map(int, input().split())
graph = [[False]*MAX for _ in range(MAX)]
visited = [False] * MAX
ans = 0

for _ in range(m):
    u,v = map(int, input().split())
    graph[u][v] = True
    graph[v][u] = True

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        ans += 1

print(ans)