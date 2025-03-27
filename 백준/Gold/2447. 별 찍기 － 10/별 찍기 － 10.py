n = int(input())

star = ['***','* *','***']
size = 3

while size < n:
    res = []
    for i in star:
        res.append(i*3)
    for j in star:
        res.append(j+' ' * size + j)
    for k in star:
        res.append(k*3)
    star = res
    size *= 3

print('\n'.join(star))