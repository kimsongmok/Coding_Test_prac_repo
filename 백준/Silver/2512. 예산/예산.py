n = int(input())
req = list(map(int, input().split()))
bud = int(input())

low = 0
high = max(req)

ans = 0
while low <= high:
  mid = (low + high) // 2
  total = 0
  
  for i in req:
    total += min(i, mid)
  
  if total <= bud:
    ans = mid
    low = mid + 1
  else:
    high = mid - 1

print(ans)