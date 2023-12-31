odd = []

for _ in range(7):
    n = int(input())
    if n % 2 != 0:
        odd.append(n)

if len(odd) != 0:
    print(sum(odd))
    print(min(odd))
else:
    print(-1)