import numpy as np

def solution(m, n, puddles):
    mod = 1000000007
    puddles = [(i - 1, j - 1) for i, j in puddles]

    matrix = np.zeros((m, n))
    matrix[0, 0] = 1

    for i in range(0, m):
        for j in range(0, n):
            if (i, j) in puddles:
                matrix[i, j] = 0
            else:
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    matrix[i, j] = matrix[0, j-1] % mod
                elif j == 0:
                    matrix[i, j] = matrix[i-1, 0] % mod
                else:
                    matrix[i, j] = matrix[i, j - 1] + matrix[i - 1, j] % mod
                    
    answer = matrix[-1, -1]

    return answer % mod