def solution(players, callings):
    nameIdx = {}
    for i in range(len(players)):
        nameIdx[players[i]] = i
    
    for j in callings:
        current = nameIdx[j]
        
        if current > 0:
            front = current - 1
            frontPlayer = players[front]
            
            players[current], players[front] = players[front], players[current]
            
            nameIdx[j] = front
            nameIdx[frontPlayer] = current
            
    return players