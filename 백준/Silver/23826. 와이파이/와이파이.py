import sys

def calc_distance(x1, y1, x2, y2):
    return abs(x2- x1) + abs(y2 - y1)
    

n = int(input())
data = []
for _ in range(n + 1):
    x, y, e = map(int, sys.stdin.readline().rstrip().split())
    data.append([x, y, e])
    
result = []
x0, y0, e0 = data[0]
for x1, y1, _ in data[1:]:
    distance = calc_distance(x0, y0, x1, y1)
    strength = max(0, e0 - distance)
    
    total_strength = 0
    for x2, y2, e in data[1:]:
        if e != 0:
            hot_spot_distance = calc_distance(x1, y1, x2, y2)
            hot_spot_strength = max(0, e - hot_spot_distance)
            total_strength += hot_spot_strength
            
    result.append(strength - total_strength)

max_value = max(result)
if max_value > 0:
    print(max_value)
else:
    print("IMPOSSIBLE")