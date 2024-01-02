n = int(input())
switch = [-1]+list(map(int, input().split()))
per = int(input())
    

def change(x):
    if switch[x] == 0:
        switch[x] = 1
    else:
        switch[x] = 0
    return

for _ in range(per):
    gender, num = map(int, input().split())
    if gender == 1:
        for i in range(num, n+1, num):
            change(i)
    else:
        change(num)
        for k in range(n//2):
            if num+k > n or num - k < 1:
                break
            if switch[num+k] == switch[num-k]:
                change(num + k)
                change(num - k)
            else:
                break

for j in range(1, n+1):
    print(switch[j], end = " ")
    if j % 20 == 0 :
        print()