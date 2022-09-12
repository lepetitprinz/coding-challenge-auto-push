from math import floor

d, h, w = map(int, input().split())
solve = (d**2 / (h**2 + w**2)) ** 0.5
s_h = floor(h * solve)
s_w = floor(w * solve)
print(f'{s_h} {s_w}')