n = int(input())
key = []
temp = []

for _ in range(n):
    s = input()
    used = False
    words = s.split()

    for i in range(len(words)):
        alpha = words[i][0].upper()
        if alpha not in temp:
            temp.append(alpha)
            words[i] = f'[{words[i][0]}]{words[i][1:]}'
            used = True
            break

    if used:
        key.append(' '.join(words))
        print(key[-1])
        continue

    for j in range(len(s)):
        alpha = s[j]
        if alpha == ' ':
            continue
        if alpha.upper() not in temp:
            temp.append(alpha.upper())
            s = s[:j] + f'[{alpha}]' + s[j+1:]
            break

    key.append(s)
    print(key[-1])