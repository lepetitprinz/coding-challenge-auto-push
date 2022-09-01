import sys

n = int(input())
for i in range(1, n+1):
    data = list(map(int, sys.stdin.readline().split()))
    k = data[0]
    scores = sorted(data[1:])
    max_score = max(scores)
    min_score = min(scores)
    gap = 0
    for j in range(k-1):
        temp = scores[j+1] - scores[j]
        if temp > gap:
            gap = temp
    print(f'Class {i}')
    print(f'Max {max_score}, Min {min_score}, Largest gap {gap}')