import sys
from math import sqrt
from itertools import combinations

def distance(p1, p2):
    x = p2[0] - p1[0]
    y = p2[1] - p1[1]
    
    return sqrt(x ** 2 + y ** 2)

test = int(input())
for _ in range(test):
    n = int(sys.stdin.readline())
    point = {}
    x_tot = 0
    y_tot = 0
    
    for i in range(n):
        x, y = map(int, sys.stdin.readline().split())
        x_tot += x
        y_tot += y
        point[i] = (x, y)
        
    lengths = []    
    for idx_list in combinations(range(n), n//2):
        x_sum = 0
        y_sum = 0
        for idx in idx_list:
            x_sum += point[idx][0]
            y_sum += point[idx][1]
        lengths.append(distance(p1=[x_sum, y_sum], p2=[x_tot - x_sum, y_tot - y_sum]))
    
    print(min(lengths))