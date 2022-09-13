from collections import Counter

def solution(nums): 
    kind_max = len(nums) // 2
    result = min(kind_max, len(Counter(nums).keys()))
    
    return result