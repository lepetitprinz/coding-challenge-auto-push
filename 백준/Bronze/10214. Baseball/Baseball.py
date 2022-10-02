import sys

input = lambda : sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    score = {'y': 0, 'k':0}
    for _ in range(9):
        y, k = map(int, input().split())
        score['y'] += y
        score['k'] += k
        
    if score['y'] > score['k']:
        print('Yonsei')
    elif score['y'] < score['k']:
        print('Korea')
    else:
        print('Draw')