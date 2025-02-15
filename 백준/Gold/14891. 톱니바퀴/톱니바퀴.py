gear = []
for _ in range(4):
    gear.append(list(input()))
n = int(input())
r = []
cnt = 0
for _ in range(n):
    num, d = map(int, input().split())
    r.append((num, d))

def rotate(num, d):
    rotation = [0] * 4
    rotation[num] = d

    for i in range(num, 0, -1):
        if gear[i][6] != gear[i-1][2]:
            rotation[i-1] = -rotation[i]
        else:
            break

    for j in range(num, 3):
        if gear[j][2] != gear[j+1][6]:
            rotation[j+1] = -rotation[j]
        else:
            break

    for k in range(4):
        if rotation[k] == -1:
            gear[k] = gear[k][1:] + [gear[k][0]]
        elif rotation[k] == 1:
            gear[k] = [gear[k][-1]] + gear[k][0:7]

for num, d in r:
    rotate(num - 1, d)

if gear[0][0] == '1':
    cnt += 1
if gear[1][0] == '1':
    cnt += 2
if gear[2][0] == '1':
    cnt += 4
if gear[3][0] == '1':
    cnt += 8

print(cnt)