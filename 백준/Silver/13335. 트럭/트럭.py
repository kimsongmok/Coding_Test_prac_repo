import sys
input = sys.stdin.readline

n, w, L = map(int, input().split())
a = [int(n) for n in input().split()]
br = [0]*w
ut = 0


while br:
    ut +=1
    br.pop(0)

    if a:
        if sum(br) + a[0] > L:
            br.append(0)
        
        else:
            br.append(a.pop(0))
        
print(ut)