while True:
    n, m = map(int, input().split())
    score = {}
    
    if n == 0 and m == 0:
        break
        
    for _ in range(n):
        ranks = list(map(int, input().split()))
        for i in ranks:
            if i not in score:
                score[i] = 0
            score[i] += 1

    score_list = list(score.items())
    max_score = max(score[j] for j in score)
    second_score = max(score[k] for k in score if score[k] < max_score)
    result = []

    for l in score:
        if score[l] == second_score:
            result.append(l)

    result.sort()
    print(' '.join(map(str, result)))