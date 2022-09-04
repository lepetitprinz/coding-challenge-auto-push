from itertools import permutations

n = int(input())
data = list(range(1, n + 1))
result = list(permutations(data, len(data)))
for r in result:
    print(*r)