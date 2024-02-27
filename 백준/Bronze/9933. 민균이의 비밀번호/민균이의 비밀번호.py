n = int(input())
li = []
for _ in range(n):
    li.append(input())

for i in li:
    if i[::-1] in li:
        print(len(i), i[len(i)//2])
        break