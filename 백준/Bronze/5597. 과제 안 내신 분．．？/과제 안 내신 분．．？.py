m = list(x for x in range(1,31))

for i in range(28):
  i = int(input())
  m.remove(i)

for j in range(len(m)):
  print(m[j])