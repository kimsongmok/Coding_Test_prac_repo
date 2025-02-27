import heapq

n = int(input())
card = []

for _ in range(n):
    card.append(int(input()))

heapq.heapify(card)

total = 0

while len(card) > 1:
    first = heapq.heappop(card)
    second = heapq.heappop(card)

    merge = first + second
    total += merge

    heapq.heappush(card, merge)
print(total)