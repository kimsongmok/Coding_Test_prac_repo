n = int(input())
time = list(map(int, input().split()))
time.sort()
ans = []


for i in range(1,n+1):
   ans.append(sum(time[:i]))

print(sum(ans))