n = 9
matrix = []
temp = []

for _ in range(n):
    mat = list(map(int,input().split()))
    matrix.append(mat)

for i in range(n):
    for j in range(len(matrix)):
        temp.append(matrix[i][j])

m_ma = max(temp)
for i in range(n):
    for j in range(len(matrix)):
        if matrix[i][j] == m_ma:
            idx = [i+1,j+1]

print(m_ma)
print(*idx)