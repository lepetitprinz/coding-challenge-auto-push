def solution(s):
    nums = list(map(int, s.split(' ')))
    nums_sorted = sorted(nums)
    result = str(nums_sorted[0]) + ' ' + str(nums_sorted[-1])
    
    return result