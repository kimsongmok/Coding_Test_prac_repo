n = int(input())
desc = [0]
q = []
for i in range(1, 10):
    q.append(i)

while q:
    num = q.pop(0)
    desc.append(num)

    last = num % 10

    for j in range(last):
        desc_num = num * 10 + j
        q.append(desc_num)


if n >= len(desc):
    print(-1)
else:
    print(desc[n])