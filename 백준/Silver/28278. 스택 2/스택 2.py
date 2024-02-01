import sys
input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    s =  input()
    if s[0] == '1':
        li.append(int(s[2:]))
    elif s[0] == '2':
        if len(li) == 0:
            print(-1)
        else:
            print(li.pop())
    elif s[0] == '3':
        print(len(li))
    elif s[0] == '4':
        if len(li) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == '5':
        if len(li) == 0:
            print(-1)
        else:
            print(li[-1])