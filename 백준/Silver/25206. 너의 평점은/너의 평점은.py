ratings ={"A+" : 4.5, "A0" : 4.0, "B+" : 3.5, "B0" : 3.0, "C+" : 2.5, "C0" : 2.0, "D+" : 1.5, "D0" : 1.0, "F" : 0 }
score_res = 0
major_res = 0

for _ in range(20):
  subj, score, rate = input().split()
  score = float(score)
  if rate != "P":
    score_res += float(score)
    major_res += score * ratings[rate]

print(major_res/score_res)