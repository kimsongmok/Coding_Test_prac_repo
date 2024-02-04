n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
visited = [False] * n
temp = []
def dfs(depth):
    v = 0
    if depth == m:
        print(' '. join(map(str, temp)))
        return
    for i in range(n):
        if li[i] != v and visited[i] == False:
            temp.append(li[i])
            v = li[i]
            visited[i] = True
            dfs(depth+1)
            temp.pop()
            visited[i] = False

dfs(0)