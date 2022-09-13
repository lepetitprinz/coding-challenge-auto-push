import numpy as np

def solution(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    result = np.sum([arr1, arr2], axis=0)
    
    answer = result.tolist()
    
    return answer