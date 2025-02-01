r, c, n = map(int, input().split())
bomb = []
even = [['O'] * c for _ in range(r)]
for _ in range(r):
  bomb.append(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bomber(bomb):
  explosion = []
  for i in range(r):
    for j in range(c):
      if bomb[i][j] == 'O':
        explosion.append((i,j))
  
  b = [['O'] * c for _ in range(r)]
  for x, y in explosion:
    b[x][y] = '.'
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if 0 <= nx < r and 0 <= ny < c:
        b[nx][ny] ='.'
  
  return b
  
ans = []
if n == 1:
  ans = bomb
elif n % 2 == 0:
  ans = even
else:
  a1 = bomber(bomb)
  a2 = bomber(a1)
  if n % 4 == 1:
    ans = a2
  if n % 4 == 3:
    ans = a1
  
for l in ans:
  print("".join(l))