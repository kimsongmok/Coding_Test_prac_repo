import heapq

V, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

dis = [float('inf')] * (V+1)
dis[k] = 0

q = []
heapq.heappush(q, (0, k))

while q:
    way, now = heapq.heappop(q)
    if dis[now] < way:
        continue
    for v, w in graph[now]:
        cost = way + w
        if cost < dis[v]:
            dis[v] = cost
            heapq.heappush(q, (cost, v))

for i in range(1, V+1):
    if dis[i] == float('inf'):
        print('INF')
    else:
        print(dis[i])