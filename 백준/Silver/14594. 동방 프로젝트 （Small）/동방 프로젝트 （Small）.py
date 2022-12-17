n = int(input())
m = int(input())
wall = set()
for _ in range(m):
    x, y = map(int, input().split())
    wall = wall.union(set(list(range(x, y))))
    
print(n - len(wall))