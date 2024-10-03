def solution(numbers):
    str_numbers = map(str, numbers)
    sorted_numbers = sorted(str_numbers, key = lambda x: x*3, reverse = True)
    
    answer = ''.join(sorted_numbers)
    
    if answer[0] == '0':
        return '0'
    else:
        return answer