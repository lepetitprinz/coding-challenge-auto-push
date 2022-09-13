def solution(s):
    answer = True
    
    s = s.lower()
    cnt_p = sum([1 for element in s if element == 'p'])
    cnt_y = sum([1 for element in s if element == 'y'])
    if cnt_p != cnt_y:
        answer = False

    return answer