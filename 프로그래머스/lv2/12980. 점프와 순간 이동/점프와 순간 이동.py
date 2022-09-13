def solution(n):
    answer = bin(n)[2:].count('1')
    return answer