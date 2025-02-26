from collections import deque

t = int(input())

for _ in range(t):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    def bfs(start):
        q = deque([start])
        visited[start] = 1

        while q:
            node = q.popleft()

            for j in graph[node]:
                if visited[j] == 0:
                    visited[j] = -visited[node]
                    q.append(j)
                elif visited[j] == visited[node]:
                    return False
        return True
    det = True

    for k in range(1, V+1):
        if visited[k] == 0:
            if not bfs(k):
                det = False
                break
    
    if det:
        print("YES")
    else:
        print("NO")