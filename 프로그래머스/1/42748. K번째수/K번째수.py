def solution(array, commands):
    answer = []
    for com in commands:
        i,j,k = com
        arr = array[i-1:j]
        arr.sort()
        answer.append(arr[k-1])
    
    return answer