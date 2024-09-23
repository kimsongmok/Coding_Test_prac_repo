T = int(input())
cnt = 0
chat = set()

for _ in range(T):
  s = input()
  if s == "ENTER":
    chat.clear()
  elif s not in chat:
    cnt+=1
    chat.add(s)
  
print(cnt)