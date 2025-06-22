inf = 10**9
t = int(input())

for _ in range(t):
    k = int(input())
    chapter = list(map(int, input().split()))

    prefix = [0] * (k + 1)
    for i in range(1, k + 1):
        prefix[i] = prefix[i-1] + chapter[i-1]

    dp = [[0] * (k+1) for _ in range(k+1)]

    for j in range(2, k + 1):
        for s in range(1, k - j + 2):
            l = s + j -1
            dp[s][l] = inf

            for i in range(s, l):
                cost = dp[s][i] + dp[i+1][l] + (prefix[l] - prefix[s-1])
                if dp[s][l] > cost:
                    dp[s][l] = cost

    print(dp[1][k])
