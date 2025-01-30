n = input()
l = len(n)

if n[0] == '0':
  print(0)
  exit(0)

dp = [0]*(l+1)
dp[0] = 1
dp[1] = 1

for i in range(2, l+1):
  if 1<= int(n[i-1:i] )<=9:
    dp[i]+=dp[i-1]
  if 10<=int(n[i-2:i])<=26:
    dp[i]+=dp[i-2]

print(dp[l]%1000000)