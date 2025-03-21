n = int(input())
cnt = 0

for _ in range(n):
    word = input()
    is_group = True

    for i in set(word):
        first = word.find(i)
        last = word.rfind(i)

        if word[first:last+1] != i*(last - first + 1):
            is_group = False
            break
    if is_group:
        cnt+=1

print(cnt)