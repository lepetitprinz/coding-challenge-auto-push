from itertools import combinations

h, w = map(int, input().split())
n = int(input())
stickers = [list(map(int, input().split())) for _ in range(n)]
cases = combinations(stickers, 2)
max_size = 0
for case in cases:
    (r1, c1), (r2, c2) = case
    if (r1+r2 <= w and max(c1, c2) <= h)\
    or (r1+c2 <= w and max(c1, r2) <= h)\
    or (c1+c2 <= w and max(r1, r2) <= h)\
    or (c1+r2 <= w and max(r1, c2) <= h)\
    or (r1+r2 <= h and max(c1, c2) <= w)\
    or (r1+c2 <= h and max(c1, r2) <= w)\
    or (c1+c2 <= h and max(r1, r2) <= w)\
    or (c1+r2 <= h and max(r1, c2) <= w):
        max_size = max(max_size, (r1*c1)+(r2*c2))
        
print(max_size)