def solution(n, w, num):

    layer = (num - 1) // w + 1
    if layer % 2 == 1:
        col = (num - 1) % w
    else:
        col = w - 1 - (num - 1) % w

    count = 1


    for i in range(layer + 1, (n - 1) // w + 2):
        if i % 2 == 1:
            upper_num = (i - 1) * w + col + 1
        else:
            upper_num = i * w - col

        if upper_num <= n:
            count += 1

    return count