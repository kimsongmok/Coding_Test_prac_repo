n = int(input())
a = list(map(int, input().split()))

nge = [-1] * n
temp = []
for i in range(n):
    while temp:
        top = temp[-1]
        if a[top] >= a[i]:
            break
        temp.pop()
        nge[top] = a[i]
    temp.append(i)
print(*nge)