while True:
  a = int(input())
  n = str(a)
  res = ''
  
  if a == 0:
    break
  else:
    for i in reversed(range(len(n))):
      res += n[i]
    
    if n == res:
      print('yes')
    else:
      print('no')