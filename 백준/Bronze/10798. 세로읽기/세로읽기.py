s = []
for _ in range(5):
    s.append(input())

for i in range(max(len(k) for k in s)):
    for j in range(5):
        if i < len(s[j]):
            print(s[j][i], end = '')