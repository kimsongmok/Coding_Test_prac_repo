import sys

n = int(input())
a = list(map(int, input().split()))
add, subtract, multiply, divide = map(int, input().split())

max_ans = -int(1e9)
min_ans = int(1e9)

def backtrack(idx, ans, add, subtract, multiply, divide):
  global max_ans, min_ans
  
  if idx == n:
    max_ans = max(max_ans, ans)
    min_ans = min(min_ans, ans)
  
  if add > 0:
    backtrack(idx+1, ans+a[idx], add - 1, subtract, multiply, divide)
  
  if subtract > 0:
    backtrack(idx+1, ans-a[idx], add, subtract - 1, multiply, divide)
  
  if multiply > 0:
    backtrack(idx+1, ans*a[idx], add, subtract, multiply - 1, divide)
  
  if divide > 0:
    if ans < 0:
      backtrack(idx+1, -(-ans // a[idx]), add, subtract, multiply, divide-1)
    else:
      backtrack(idx+1, ans//a[idx], add, subtract, multiply, divide-1)

backtrack(1, a[0], add, subtract, multiply, divide)

print(max_ans)
print(min_ans)