from collections import Counter

def solution(participant, completion):
    
    answer = ''
    cnt_part = Counter(participant)
    cnt_comp = Counter(completion)
    result = (cnt_part - cnt_comp).keys()
    answer = list(result)[0]
    
    return answer