t = int(input())

for _ in range(t):
  t_i = int(input())
  team_num = list(map(int, input().split()))
  
  cnt = {}
  for i in team_num:
    if i not in cnt:
      cnt[i] = 0
    cnt[i] += 1
  
  valid = []
  for j in cnt:
    if cnt[j] == 6:
      valid.append(j)
  
  ranks = {}
  rank = 1
  for k in team_num:
    if k in valid:
      if k not in ranks:
        ranks[k] = []
      ranks[k].append(rank)
      rank += 1
  
  best_team = -1
  best_sum = 10**9
  best_5th = 10**9

  for l in valid:
      s4 = ranks[l][0] + ranks[l][1] + ranks[l][2] + ranks[l][3]
      r5 = ranks[l][4]
      if s4 < best_sum or (s4 == best_sum and r5 < best_5th):
          best_team = l
          best_sum = s4
          best_5th = r5

  print(best_team)