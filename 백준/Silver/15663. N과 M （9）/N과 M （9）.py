from itertools import permutations

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

perm = set(permutations(numbers, m))
for p in sorted(perm):
    print(' '.join(map(str, p)))