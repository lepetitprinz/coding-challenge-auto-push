from string import ascii_uppercase
from itertools import combinations

seq = input()

loc = {}
for i, alpha in enumerate(seq):
    if alpha in loc:
        loc[alpha].append(i)
    else:
        loc[alpha] = [i]

count = 0
for x, y in combinations(ascii_uppercase, 2):
    x1, x2 = loc[x] 
    y1, y2 = loc[y]
    if (x1 < y1 < x2 < y2) or (y1 < x1 < y2 < x2):
        count += 1

print(count)