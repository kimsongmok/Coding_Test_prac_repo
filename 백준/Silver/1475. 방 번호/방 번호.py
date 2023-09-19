s = input()
visited = [0]*10
for i in s:
    x = int(i)
    if x == 6 or x == 9:
        if visited[6] <= visited[9]:
            visited[6]+=1
        else:
            visited[9]+=1
    else:
        visited[x]+=1
print(max(visited))