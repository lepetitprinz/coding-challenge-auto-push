from math import gcd

def solution(n, m):
    a = gcd(n, m)
    b = n * m // a
    answer = [a, b]
    
    return answer