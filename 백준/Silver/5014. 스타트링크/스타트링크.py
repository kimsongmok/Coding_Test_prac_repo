from collections import deque

def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        v = q.popleft()
        if v == g:
            return cnt[g]
        for i in (v+u, v-d):
            if 0< i <=f and not visited[i]:
                visited[i] = True
                cnt[i] = cnt[v]+1
                q.append(i)
    if cnt[g] == 0:
        return "use the stairs"

f,s,g,u,d = map(int,input().split()) #총:F, 현재:S, 목표:G, 올라가는 수:U, 내려가는 수:D
visited = [False for i in range(f+1)]
cnt = [0 for i in range(f+1)]
print(bfs(s))