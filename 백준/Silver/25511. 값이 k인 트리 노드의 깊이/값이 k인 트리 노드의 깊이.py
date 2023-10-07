from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 5)
input = stdin.readline

def dfs(tree, values, current, depth, target):
    if values[current] == target:
        return depth
    if current not in tree:
        return -1

    for child in tree[current]:
        found_depth = dfs(tree, values, child, depth + 1, target)
        if found_depth != -1:
            return found_depth
    return -1


n, k = map(int, input().split())

tree = {}
for _ in range(n - 1):
    parent, child = map(int, input().split())
    if parent not in tree:
        tree[parent] = []
    tree[parent].append(child)

values = list(map(int, input().split()))

print(dfs(tree, values, 0, 0, k))
