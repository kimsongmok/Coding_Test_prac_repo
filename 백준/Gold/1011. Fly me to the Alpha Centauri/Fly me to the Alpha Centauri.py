t = int(input())
res =[]

for _ in range(t):
    x, y = map(int, input().split())
    dis = y - x
    max_k = int(dis ** 0.5)

    if max_k ** 2 == dis:
        res.append(2*max_k-1)
    elif dis <= max_k * (max_k+1):
        res.append(2*max_k)
    else:
        res.append(2*max_k+1)

for i in range(len(res)):
    print(res[i])
