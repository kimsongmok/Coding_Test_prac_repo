r, c, k = map(int, input().split())
road = [list(input()) for _ in range(r)]

visited = [[False]*c for _ in range(r)]
ans = 0

def dfs(x, y, dist):
  if x == 0 and y == c-1:
    if dist == k:
      global ans
      ans += 1
    return
  
  remain = x + (c-1 - y)
  if dist + remain > k:
    return

  if x+1 < r and road[x+1][y] == '.' and not visited[x+1][y]:
      visited[x+1][y] = True
      dfs(x+1, y, dist+1)
      visited[x+1][y] = False
  if x-1 >= 0 and road[x-1][y] == '.' and not visited[x-1][y]:
      visited[x-1][y] = True
      dfs(x-1, y, dist+1)
      visited[x-1][y] = False
  if y+1 < c and road[x][y+1] == '.' and not visited[x][y+1]:
      visited[x][y+1] = True
      dfs(x, y+1, dist+1)
      visited[x][y+1] = False
  if y-1 >= 0 and road[x][y-1] == '.' and not visited[x][y-1]:
      visited[x][y-1] = True
      dfs(x, y-1, dist+1)
      visited[x][y-1] = False
if road[r-1][0] == 'T' or road[0][c-1] == 'T':
  print(0)
else:
  visited[r-1][0] = True
  dfs(r-1, 0, 1)
  print(ans)