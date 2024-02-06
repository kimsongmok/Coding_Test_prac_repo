import sys
sys.setrecursionlimit(10**3)
input = sys.stdin.readline
MAX = 100+10

def dfs(idx, count):
    global visited, graph, end, answer
    visited[idx] = True
    if idx == end:
        answer = count
        return
    
    for i in range(1, n+1):
        if not visited[i] and graph[idx][i]:
            dfs(i, count + 1)

# 0. 입력 및 초기화
n = int(input())
start, end = map(int, input().split())
m = int(input())
graph = [[False] * MAX for _ in range(MAX)]
visited = [False] * MAX
answer = -1

# 1. graph에 연결 정보 채우기
for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True

# 2. DFS호출
dfs(start, 0)

# 3. 출력
print(answer)