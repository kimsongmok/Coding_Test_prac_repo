n = int(input())
skyline = []
cnt = 0

for _ in range(n):
    x, y = map(int, input().split())

    while skyline and skyline[-1] > y:
        skyline.pop()
        cnt += 1

    if y > 0 and (not skyline or skyline[-1] != y):
        skyline.append(y)

cnt += len(skyline)

print(cnt)
