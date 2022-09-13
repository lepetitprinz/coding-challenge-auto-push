import sys
sys.setrecursionlimit(10**7)
from functools import lru_cache

def solution(n):
    return fibo(n) % 1234567


@lru_cache(maxsize=None)
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)