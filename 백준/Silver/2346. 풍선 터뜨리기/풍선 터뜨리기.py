import sys
input = sys.stdin.readline

n = int(input())
popping = list(enumerate(map(int, input().split())))
idx = 0

while popping:
    ans = popping.pop(idx)
    print(ans[0]+1,end= ' ')
    
    if ans[1] < 0 and popping:
        idx = (idx + ans[1]) % len(popping)
    elif ans[1] > 0 and popping:
        idx = (idx + (ans[1]-1)) % len(popping)