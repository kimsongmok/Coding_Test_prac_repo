n, w, L = map(int, input().split())
truck = list(map(int, input().split()))

br = [0] * w
ut = 0

while br:
    ut +=1
    br.pop(0)

    if truck:
        if sum(br) + truck[0] > L:
            br.append(0)
        else:
            br.append(truck.pop(0))

print(ut)