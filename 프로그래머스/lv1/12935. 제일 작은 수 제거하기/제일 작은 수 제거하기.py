def solution(arr):
    min_val = min(arr)
    arr.remove(min_val)
    if len(arr) == 0:
        arr = [-1]
        
    return arr