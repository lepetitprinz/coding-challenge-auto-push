import sys
from math import gcd

input = lambda: sys.stdin.readline().rstrip()

def solution(m, n, x, y):
    lcm = m * n // gcd(m, n)

    result = -1
    left = x
    right = y
    while left <= lcm:
        if left == right:
            result = left
            break
        elif left > right:
            right += n
        else:
            left += m

    return result


test = int(input())
for _ in range(test):
    m, n, x, y = map(int, input().split())
    result = solution(m, n, x, y)
    print(result)
