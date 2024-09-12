def solution(a, b):
    a_s = str(a)
    b_s = str(b)
    
    res1 = int(a_s + b_s)
    res2 = int(b_s + a_s)
    
    if res1 > res2:
        return res1
    elif res1 < res2:
        return res2
    elif res1 == res2:
        return res1