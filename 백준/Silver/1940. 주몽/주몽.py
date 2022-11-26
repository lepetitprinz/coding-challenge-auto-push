n = int(input())
m = int(input())
data = set(sorted(list(map(int, input().split()))))

match = 0
for num in data:
    if m - num in data:
        match += 1
    
print(match // 2)