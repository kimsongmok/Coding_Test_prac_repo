n = int(input())
cookie = [list(input()) for _ in range(n)]

head = None
for i in range(n):
    for j in range(n):
        if cookie[i][j] == '*':
            head = (i, j)
            break
    if head is not None:
        break

heart = (head[0]+1, head[1])
hx, hy = heart

left = 0
for k in range(hy - 1, -1, -1):
  if cookie[hx][k] == '*':
    left += 1
  else:
    break

right = 0
for l in range(hy+1, n):
  if cookie[hx][l] == '*':
    right += 1
  else:
    break

waist = 0
x = hx + 1
while x < n and cookie[x][hy] == '*':
  waist += 1
  x += 1

leg_start = hx + waist + 1

left_leg = 0
for m in range(leg_start, n):
  if cookie[m][hy-1] == '*':
    left_leg += 1
  
  else:
    break

right_leg = 0
for i in range(leg_start, n):
  if cookie[i][hy+1] == '*':
    right_leg += 1
  
  else:
    break

print(hx+1, hy+1)
print(left, right, waist, left_leg, right_leg)