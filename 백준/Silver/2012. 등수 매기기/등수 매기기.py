n = int(input())
expect = []
for _ in range(n):
  expect.append(int(input()))

expect.sort()

ans = 0

for i in range(1, n+1):
  ans += abs(expect[i-1]-i)

print(ans)