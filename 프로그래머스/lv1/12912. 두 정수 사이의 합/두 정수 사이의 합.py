def solution(a, b):
    if a <= b:
        nums = [num for num in range(a, b+1)]
    else:
        nums = [num for num in range(a, b-1, -1)]
    return sum(nums)