from itertools import combinations

data = []
for _ in range(9):
    data.append(int(input()))
    
result = []
for c in combinations(data, 7):
    if sum(c) == 100:
        result = c
        break

result = sorted(result)
for num in result:
    print(num)