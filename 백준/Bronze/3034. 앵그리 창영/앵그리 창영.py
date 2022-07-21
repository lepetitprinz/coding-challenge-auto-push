import sys
from math import sqrt

n, w, h = map(int, input().split())
diagonal = sqrt(w**2 + h**2)
for _ in range(n):
    if int(sys.stdin.readline()) <= diagonal:
        print('DA')
    else:
        print('NE')