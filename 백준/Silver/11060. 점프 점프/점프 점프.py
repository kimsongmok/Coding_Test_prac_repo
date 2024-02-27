from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
graph = list(map(int, input().split()))
visited = [0]*(n+1)


if n == 1:
    print(0)

else:
    q = deque([1])
    
    while q:
        x = q.popleft()
        if x + graph[x-1] >= n:
            print(visited[x]+1)
            break
        for i in range(1, graph[x-1]+1):
            nx = x+i
            if visited[nx] == 0:
                q.append(nx)
                visited[nx] = visited[x]+1
    else:
        print(-1)
        