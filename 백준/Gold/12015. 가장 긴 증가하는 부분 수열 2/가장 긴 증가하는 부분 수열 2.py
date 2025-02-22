n = int(input())
seq = list(map(int, input().split()))

lis = []

for i in seq:
    l, r = 0, len(lis)

    while l < r:
        mid = (l + r)//2
        if lis[mid] >= i:
            r = mid
        else:
            l = mid + 1

    if l == len(lis):
        lis.append(i)
    else:
        lis[l] = i

print(len(lis))