n, m = map(int, input().split())
li = list(map(int, input().split()))
cnt = 0
ans = []

def dev_sum(start):
    global cnt
    if sum(ans) == m and len(ans)>0:
        cnt+=1
    
    for i in range(start,n):
        ans.append(li[i])
        dev_sum(i+1)
        ans.pop()

dev_sum(0)
print(cnt)