from itertools import product

def backtrack(data, m):
    sorted_data = sorted(data)
    result = product(sorted_data, repeat = m)
    
    return result

n, m = map(int, input().split())
data = list(map(int, input().split()))
result = backtrack(data, m)

for row in result:
    print(*row)

print(*result, sep='\n')