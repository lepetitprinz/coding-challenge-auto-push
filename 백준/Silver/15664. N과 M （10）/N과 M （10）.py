from itertools import combinations

def backtrack(data, m):
    sorted_data = sorted(data)
    result = set(combinations(sorted_data, m))
    
    return sorted(list(result))

n, m = map(int, input().split())
data = list(map(int, input().split()))
result = backtrack(data, m)

for row in result:
    print(*row)