d1, d2, d3 = map(int,input().split())

if d1==d2==d3:
    print(10000+(1000*d1))
elif d1==d2 or d2==d3 or d1==d3:
    if d1 == d2:
        print(1000+(100*d1))
    if d2 == d3:
        print(1000+(100*d2))
    if d1 == d3:
        print(1000+(100*d1))
else:
    print(max(d1, d2, d3)*100)