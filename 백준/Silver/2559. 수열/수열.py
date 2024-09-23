import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temp = list(map(int, input().split()))

temp_s = sum(temp[:k])
max_temps = temp_s

for i in range(1, n-k+1):
  temp_s = temp_s - temp[i-1] + temp[i+k-1]
  max_temps = max(temp_s, max_temps)

print(max_temps)
