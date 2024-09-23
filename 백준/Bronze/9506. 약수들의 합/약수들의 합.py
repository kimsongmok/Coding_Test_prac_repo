while True:
  n = int(input())
  d = []
  if n == -1:
    break
  for i in range(1,n):
    if n%i == 0:
      d.append(i)
  if sum(d) == n:
    print(n,' = ' + ' + '.join(str(i) for i in d),sep="")
  else:
    print(n, "is NOT perfect.")
