from math import gcd

def least_common_multiple(x, y):
    return x * y // gcd(x, y)

def solution(arr):
    while True:
        arr.append(least_common_multiple(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]