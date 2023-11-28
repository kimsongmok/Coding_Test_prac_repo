from itertools import combinations

n, m = map(int, input().split())
black_j = list(map(int,input().split()))
com = list(combinations(black_j,3))
temp = []

for i in com:
    if sum(i) <= m:
        temp.append(sum(i))

print(max(temp))