n = int(input())
city = list(map(int, input().split()))
oil = list(map(int, input().split()))

def gasStation(n, length, price):
  
  total = 0
  minimum = price[0]

  for i in range(n-1):
    total += minimum * length[i]
    if price[i+1] < minimum:
      minimum = price[i+1]
    
  return total

print(gasStation(n, city, oil))