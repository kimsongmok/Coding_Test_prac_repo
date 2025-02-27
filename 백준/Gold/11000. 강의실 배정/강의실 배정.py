import heapq

n = int(input())
lecture = []

for _ in range(n):
    s,t = map(int, input().split())
    lecture.append([s, t])

lecture.sort()

room = []
heapq.heappush(room, lecture[0][1])
for i in range(1, n):
    start, end = lecture[i]

    if room[0] <= start:
        heapq.heappop(room)

    heapq.heappush(room, end)

print(len(room))