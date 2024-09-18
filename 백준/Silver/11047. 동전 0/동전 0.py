import sys
input = sys.stdin.readline

n, k = map(int, input().split())
w = []
cnt = 0

for _ in range(n):
  w.append(int(input()))
w.sort(reverse=True)

for i in w:
  if k >= i:
    cnt += k//i
    k %= i
    if k <= 0:
      break

print(cnt)
    