import sys
from itertools import permutations

n = int(input())
k = int(input())
data = [sys.stdin.readline().rstrip() for _ in range(n)]

result = set()
for comb in permutations(data, k):
    result.add(''.join(comb))

print(len(result))