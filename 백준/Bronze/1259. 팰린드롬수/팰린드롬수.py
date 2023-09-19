while True:
    n = int(input())
    s = str(n)
    a = ''
    if n == 0:
        break
    else:
        for i in reversed(range(len(s))):
            a += s[i]
        if a == s:
            print('yes')
        else:
            print('no')