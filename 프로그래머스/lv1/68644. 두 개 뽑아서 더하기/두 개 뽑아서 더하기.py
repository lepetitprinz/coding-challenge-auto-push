from itertools import combinations

def solution(numbers):
    result = [x + y for x, y in combinations(numbers, 2)]
    result = list(set(result))
    result = sorted(result)
    
    return result