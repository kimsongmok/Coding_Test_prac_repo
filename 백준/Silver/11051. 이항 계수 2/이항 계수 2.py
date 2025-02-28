def factorial(c):
    result = 1
    for i in range(2, c + 1):
        result *= i
    return result

n, k = map(int, input().split())

num = factorial(n)
res = factorial(k) * factorial(n-k)

print((num // res) % 10007)