from itertools import combinations

def backtrack(data, m):
    data = sorted(data)
    comb_data = combinations(data, m)
    comb_data = sorted(list(set(comb_data)))
    
    return comb_data
    
n, m = map(int, input().split())
data = list(map(int, input().split()))

result = backtrack(data, m)

for row in result:
    print(*row)