t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    color = [0] * (n + 1)

    for _ in range(m):
        x, y = list(map(int, input().split()))
        graph[x].append(y)
        graph[y].append(x)

    is_possible = True
    circle = []

    for i in range(1, n + 1):
        if color[i] == 0:
            circle.append(i)
            color[i] = 1

            while circle:
                now = circle.pop()

                for j in graph[now]:
                    if color[j] == 0:
                        color[j] = -color[now]
                        circle.append(j)
                    elif color[j] == color[now]:
                        is_possible = False
                        break

                if not is_possible:
                    break

        if not is_possible:
            break

    if is_possible:
        print("possible")
    else:
        print("impossible")

