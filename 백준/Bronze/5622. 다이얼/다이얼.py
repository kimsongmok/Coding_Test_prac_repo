alpha = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
a = input()
cnt = 0

for i in range(len(a)):
  for j in alpha:
    if a[i] in j:
      cnt += alpha.index(j)+3

print(cnt)