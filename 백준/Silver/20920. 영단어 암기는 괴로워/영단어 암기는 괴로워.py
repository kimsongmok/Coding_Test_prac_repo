import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())

word = []

for _ in range(n):
  s = input().rstrip()
  word.append(s)

counter = Counter(i for i in word if len(i) >= m)
words = list(counter)

words.sort()

words.sort(key=len, reverse=True)

words.sort(key=counter.get, reverse= True)

print("\n".join(words))