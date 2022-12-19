import sys

input = lambda: sys.stdin.readline().rstrip()

def make_coor_map():
    coor_to_val = {}
    val_to_coor = {}
    v = 1
    for i in range(1, 300):
        for j in range(1, i):
            x = j
            y = i - j
            coor_to_val[(x, y)] = v
            val_to_coor[v] = (x, y)
            v += 1
            
    return coor_to_val, val_to_coor

def solve(prob, coor_to_val, val_to_coor):
    results = []
    for a, b in prob:
        x1, y1 = val_to_coor[a]
        x2, y2 = val_to_coor[b]
        
        result = coor_to_val[(x1 + x2, y1 + y2)]
        results.append(result)

    return results
    
t = int(input())
prob = []
for _ in range(t):
    a, b = map(int, input().split())
    prob.append((a, b))
    
coor_to_val, val_to_coor = make_coor_map()
results = solve(prob, coor_to_val, val_to_coor)
print(*results, sep='\n')