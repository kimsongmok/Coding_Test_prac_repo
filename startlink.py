INF = 99999
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [False for _ in range(n)]
min_ = INF

def dfs(l,idx):
    global min_
    if l == n//2:
        t1, t2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    t1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    t2 += graph[i][j]
        min_ = min(min_, abs(t1-t2))
        return

    for i in range(idx,n):
        if not visited[i]:
            visited[i] = True
            dfs(l+1,i+1)
            visited[i] = False


dfs(0,0)
print(min_)