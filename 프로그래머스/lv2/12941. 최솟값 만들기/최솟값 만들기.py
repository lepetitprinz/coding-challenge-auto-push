from itertools import permutations
import numpy as np

def solution(A, B):
    A = sorted(A)
    B = sorted(B, reverse=True)
    
    result = np.dot(A, B)
    return int(result)