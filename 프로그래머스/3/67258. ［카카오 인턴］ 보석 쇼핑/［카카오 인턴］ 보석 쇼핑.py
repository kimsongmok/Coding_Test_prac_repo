def solution(gems):
    answer = []
    short = len(gems)+1
    l = 0
    r = 0
    check_len = len(set(gems))
    gem_dics = {}
    
    while r < len(gems):
        
        if gems[r] not in gem_dics:
            gem_dics[gems[r]] = 1
        else:
            gem_dics[gems[r]] += 1
        r += 1
        
        if len(gem_dics) == check_len:
            while l < r:
                if gem_dics[gems[l]]>1:
                    gem_dics[gems[l]] -= 1
                    l += 1
                
                elif short > r - l:
                    short = r - l
                    answer = [l+1,r]
                    break
                else:
                    break
                
    return answer