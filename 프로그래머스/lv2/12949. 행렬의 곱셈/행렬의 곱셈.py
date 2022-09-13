import numpy as np

def solution(arr1, arr2):
    ar1 = np.array(arr1)
    ar2 = np.array(arr2)
    mat_mul = np.matmul(arr1, arr2)
    
    return mat_mul.tolist()