n, m = map(int, input().split())
truth = list(map(int, input().split()))
parties = []

for _ in range(m):
    parties.append(list(map(int, input().split()))[1:])

know_truth = []
for i in range(1, len(truth)):
    know_truth.append(truth[i])

group = [i for i in range(n + 1)]

for party in parties:
    for i in range(len(party) - 1):
        a = party[i]
        b = party[i + 1]

        x = a
        while group[x] != x:
            group[x] = group[group[x]]
            x = group[x]
        root_a = x

        x = b
        while group[x] != x:
            group[x] = group[group[x]]
            x = group[x]
        root_b = x

        if root_a != root_b:
            group[root_b] = root_a

truth_groups = []
for person in know_truth:
    x = person
    while group[x] != x:
        group[x] = group[group[x]]
        x = group[x]
    truth_groups.append(x)

cnt = 0
for party in parties:
    possible = True
    for person in party:
        x = person
        while group[x] != x:
            group[x] = group[group[x]]
            x = group[x]
        if x in truth_groups:
            possible = False
            break
    if possible:
        cnt += 1

print(cnt)